from plugin import AudioLDMPlugin
from tuneflow_devkit import Runner
from pathlib import Path
import uvicorn

app = Runner(plugin_class_list=[AudioLDMPlugin], bundle_file_path=str(
    Path(__file__).parent.joinpath('bundle.json').absolute())).start(path_prefix='/plugins/audio-ldm')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
