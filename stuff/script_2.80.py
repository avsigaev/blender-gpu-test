import bpy
import sys
import json

argv = sys.argv[sys.argv.index("--") + 1:]
args = argv[0]
params = json.loads(args)

print('ARGv %s' % argv)
print('ARGs %s' % args)
print('params %s' % params)

scene_name = params['scene']
camera_name = params['camera']
res_x = params['res_x']
res_y = params['res_y']
samples = params.get('samples', 0)
run_mode = params['run_mode']
result_dir = params['result_dir']

print('[SONM] Rendering scene `{}`, camera `{}`, {}x{} {} smpl, (mode = {})'.format(
    scene_name, camera_name, res_x, res_y, samples, run_mode))

ctx = bpy.context
scene = ctx.scene

cam = None
for obj in scene.objects:
    if obj.type == 'CAMERA':
        if obj.name == camera_name:
            cam = obj

if not cam:
    print('[SONM] CRITICAL:  unable to find camera `{}` for scene `{}`'.format(scene_name, camera_name))
    sys.exit(10)

print('[SONM] camera found: `{}`'.format(cam))
print('[SONM] scene found: `{}`'.format(scene))
print('[SONM] result dir: `{}`'.format(result_dir))

render = scene.render
render.filepath = result_dir

wrong_formats = ['', 'AVI_JPEG', 'AVI_RAW', 'FFMPEG']
if render.image_settings.file_format in wrong_formats:
    render.image_settings.file_format = 'PNG'
print('[SONM] file_format = {}, color_mode = {}'.format(
    render.image_settings.file_format,
    render.image_settings.color_mode))

render.resolution_percentage = 100
render.resolution_x = res_x
render.resolution_y = res_y
scene.camera = cam
if samples > 0:
    scene.cycles.samples = samples
    scene.cycles.aa_samples = samples
    scene.cycles.use_square_samples = False

scene.cycles.device = 'GPU'
render.threads_mode = 'AUTO'
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'

c_perf = bpy.context.preferences.addons['cycles'].preferences
# this magic line refreshes device list visible by blender,
# and gives us ability to use GPU and CPU and OpenCL.
c_perf.get_devices()

if run_mode == 'analysis':
    print('[SONM] only one device')
    for dev in c_perf.devices:
        print('[SONM] disabling device "%s"...' % dev.name)
        dev.use = False

    for dev in c_perf.devices:
        print('[SONM] enabling only "%s"...' % dev.name)
        dev.use = True
        break
else:
    print('[SONM] enabling all of %d devices' % len(c_perf.devices))
    for dev in c_perf.devices:
        print('[SONM] trying to enable device "%s"' % dev.name)
        dev.use = dev.type == 'CUDA'

for dev in c_perf.devices:
    print('[SONM] device "%s" enabled? %s' % (dev.name, dev.use))
