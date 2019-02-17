import json
import os
import logging
import string
import escapism
from kubespawner.spawner import KubeSpawner
from jhub_remote_user_authenticator.remote_user_auth import RemoteUserAuthenticator
#from oauthenticator.github import GitHubOAuthenticator

SERVICE_ACCOUNT_SECRET_MOUNT = '/var/run/secrets/sa'


class KubeFormSpawner(KubeSpawner):

    def _options_form_default(self):
        global registry, repoName
        return '''
    <script defer src='https://use.fontawesome.com/releases/v5.3.1/js/solid.js' integrity='sha384-GJiigN/ef2B3HMj0haY+eMmG4EIIrhWgGJ2Rv0IaWnNdWdbWPr1sRLkGz7xfjOFw' crossorigin='anonymous'></script>
    <script defer src='https://use.fontawesome.com/releases/v5.3.1/js/brands.js' integrity='sha384-2vdvXGQdnt+ze3ylY5ESeZ9TOxwxlOsldUzQBwtjvRpen1FwDT767SqyVbYrltjb' crossorigin='anonymous'></script>
    <script defer src='https://use.fontawesome.com/releases/v5.3.1/js/fontawesome.js' integrity='sha384-2OfHGv4zQZxcNK+oL8TR9pA+ADXtUODqGpIRy1zOgioC4X3+2vbOAp5Qv7uHM4Z8' crossorigin='anonymous'></script>
    <br>
    <div class='form-group'>
    <label for='inputDockerImage'><i class='fab fa-docker'></i> Docker Image</label>
    <input class='form-control' list='list_images' name='inputDockerImage' aria-describedby='imgHelp' placeholder='nvaitc/ai-lab:latest' value=''>
    <datalist id='list_images'>
      <option value='nvaitc/ai-lab:latest'>
    </datalist>
    <p><small id='imgHelp' class='form-text text-muted'>You can use any JupyterHub compatible Docker image from Docker Hub. The default image is <code>nvaitc/ai-lab:latest</code>, which includes most typical packages required for deep learning: TensorFlow, Keras, PyTorch, MXNet, RAPIDS, NLTK, OpenCV.
    </small></p>
    </div>
    <div class='form-group'>
    <label for='cpu_guarantee'><i class='fas fa-microchip'></i> vCPU Threads</label>
    <input type='text' class='form-control' name='cpu_guarantee' aria-describedby='cpuHelp' placeholder='2.0'>
    <p><small id='cpuHelp' class='form-text text-muted'>If your work is not CPU-intensive, you can choose less than 1 CPU (e.g. <code>0.5</code>)</small></p>
    </div>
    <div class='form-group'>
    <label for='mem_limit'><i class='fas fa-memory'></i> Reserved Memory</label>
    <input type='text' class='form-control' name='mem_limit' aria-describedby='memHelp' placeholder='8.0Gi'>
    <p><small id='memHelp' class='form-text text-muted'>Total amount of reserved RAM (e.g. <code>7.5Gi</code>). Your Notebook may consume more if system resources allow.</small></p>
    </div>
    <div class='form-group'>
    <label for='extra_resource_limits'><i class='fas fa-ticket-alt'></i> Reserved GPU</label>
    <input class='form-control' list='extra_resource_limits' name='extra_resource_limits' placeholder='{{&quot;nvidia.com/gpu&quot;: 0}}' value='{{&quot;nvidia.com/gpu&quot;: 1}}'>
    <datalist id='extra_resource_limits'>
      <option value='{{&quot;nvidia.com/gpu&quot;: 0}}'>
      <option value='{{&quot;nvidia.com/gpu&quot;: 1}}'>
      <option value='{{&quot;nvidia.com/gpu&quot;: 2}}'>
      <option value='{{&quot;nvidia.com/gpu&quot;: 3}}'>
      <option value='{{&quot;nvidia.com/gpu&quot;: 4}}'>
    </datalist>
    <p><small id='memHelp'>Example: to reserve 2 GPUs: <code>{{&quot;nvidia.com/gpu&quot;: 2}}</code><br>
    To reserve no GPU, please use <code>{{&quot;nvidia.com/gpu&quot;: 0}}</code>.</small></p>
    </div>
    <br>
    <div class='alert alert-warning' role='alert'>
    <p>If your Notebook is unable to start, it is likely that the GPU you requested for is not available.<br>
    Try starting a Notebook <b>without a GPU</b> before reporting a server problem!</p>
    <div>
    <br>
    '''.format(registry, repoName)

    def options_from_form(self, formdata):
        options = {}
        options['image'] = formdata.get('inputDockerImage', [''])[0].strip()
        options['cpu_guarantee'] = formdata.get(
                'cpu_guarantee', [''])[0].strip()
        options['mem_limit'] = formdata.get(
                'mem_limit', [''])[0].strip()
        options['extra_resource_limits'] = formdata.get(
                'extra_resource_limits', [''])[0].strip()
        logging.info(options)
        return options

    @property
    def singleuser_image_spec(self):
        if self.user_options.get('image'):
            image = self.user_options['image']
        else:
            image = 'nvaitc/ai-lab:latest'
        return image

    @property
    def cpu_guarantee(self):
        cpu = '2.0'
        if self.user_options.get('cpu_guarantee'):
            cpu = self.user_options['cpu_guarantee']
        return cpu

    @property
    def mem_limit(self):
        mem = '8.0Gi'
        if self.user_options.get('mem_limit'):
            mem = self.user_options['mem_limit']
        return mem

    @property
    def extra_resource_limits(self):
        extra = ''
        if self.user_options.get('extra_resource_limits'):
            extra = json.loads(self.user_options['extra_resource_limits'])
        return extra

    def _parse_user_name(self, username):
        safe_chars = set(string.ascii_lowercase + string.digits)
        name = username.split(':')[-1]
        legacy = ''.join([s if s in safe_chars else '-' for s in name.lower()])
        safe = escapism.escape(name, safe=safe_chars, escape_char='-').lower()
        return legacy, safe, name

    def _expand_user_properties(self, template):
        # override KubeSpawner method to remove prefix accounts.google: for iap
        # and truncate to 63 characters

        # Set servername based on whether named-server initialised
        if self.name:
            servername = '-{}'.format(self.name)
        else:
            servername = ''

        legacy, safe, name = self._parse_user_name(self.user.name)
        rname = template.format(
            userid=self.user.id,
            username=safe,
            unescaped_username=name,
            legacy_escape_username=legacy,
            servername=servername
        )[:63]
        return rname


###################################################
# JupyterHub Options
###################################################
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
# Don't try to cleanup servers on exit - since in general for k8s, we want
# the hub to be able to restart without losing user containers
c.JupyterHub.cleanup_servers = False
###################################################

c.JupyterHub.services = [
    {
        'name': 'wget-cull-idle',
        'admin': True,
        'command': ['wget', 'https://raw.githubusercontent.com/jupyterhub/jupyterhub/master/examples/cull-idle/cull_idle_servers.py', '-N']
    },
    {
        'name': 'cull-idle',
        'admin': True,
        'command': ['python', 'cull_idle_servers.py', '--timeout=14400']
    }
]

###################################################
# Spawner Options
###################################################
cloud = os.environ.get('CLOUD_NAME')
registry = os.environ.get('REGISTRY')
repoName = os.environ.get('REPO_NAME')
c.JupyterHub.spawner_class = KubeFormSpawner
c.KubeSpawner.singleuser_image_spec = '{0}/{1}/tensorflow-notebook'.format(registry, repoName)

c.KubeSpawner.cmd = 'start-singleuser.sh'
c.KubeSpawner.args = ['--allow-root']
# gpu images are very large ~15GB. need a large timeout.
c.KubeSpawner.start_timeout = 60 * 30
# Increase timeout to 5 minutes to avoid HTTP 500 errors on JupyterHub
c.KubeSpawner.http_timeout = 60 * 5

# Volume setup
c.KubeSpawner.singleuser_uid = 1000
c.KubeSpawner.singleuser_fs_gid = 100
c.KubeSpawner.singleuser_working_dir = '/home/jovyan'
volumes = []
volume_mounts = []

###################################################
# Persistent volume options
###################################################
pvc_mount = os.environ.get('NOTEBOOK_PVC_MOUNT')
if pvc_mount and pvc_mount != 'null':
    c.KubeSpawner.user_storage_pvc_ensure = True
    c.KubeSpawner.user_storage_capacity = '100Gi'
    c.KubeSpawner.user_storage_class = 'nfs-client'
    c.KubeSpawner.user_storage_access_modes = ['ReadWriteMany']
    c.KubeSpawner.pvc_name_template = 'claim-{username}{servername}'

    # user volume
    volumes.append(
            {
            'name': 'volume-{username}{servername}',
            'persistentVolumeClaim': {
                'claimName': 'claim-{username}{servername}'
            }
        }
    )
    volume_mounts.append(
        {
            'mountPath': pvc_mount,
            'name': 'volume-{username}{servername}'
        }
    )

# Extra PVCs defined by env
pvcs = os.environ.get('KF_PVC_LIST')
if pvcs and pvcs != 'null':
    for pvc in pvcs.split(','):
        volumes.append({
            'name': pvc,
            'persistentVolumeClaim': {
                'claimName': pvc
            }
        })
        volume_mounts.append({
            'name': pvc,
            'mountPath': pvc_mount + '/' + pvc
        })

c.KubeSpawner.volumes = volumes
c.KubeSpawner.volume_mounts = volume_mounts

######## Authenticator ######
# Authenticator
if os.environ.get('KF_AUTHENTICATOR') == 'iap':
    c.JupyterHub.authenticator_class = 'jhub_remote_user_authenticator.remote_user_auth.RemoteUserAuthenticator'
    c.RemoteUserAuthenticator.header_name = 'x-goog-authenticated-user-email'
else:
    c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

try:
    if os.environ.get('DEFAULT_JUPYTERLAB').lower() == 'true':
        c.KubeSpawner.default_url = '/lab'

except Exception as e:
    print('DEFAULT_JUPYTERLAB', e)
