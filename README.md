# AudioLDM TuneFlow Plugin

Fork of https://github.com/haoheliu/AudioLDM as a TuneFlow Plugin

<img src="./images/audioldm_cn.gif" width="500" />

## Usage

Steps to run the plugin:

0. Install **TuneFlow Desktop** by downloading the app from https://tuneflow.com

1. Clone this repo

``` bash
git clone https://github.com/tuneflow/AudioLDM.git
```

2. cd to the repo folder, and install dependencies using:

```bash
pip install -r requirements.txt
```

> **Note:** It is highly recommended to create a venv to run this plugin.

3. Download the model from https://huggingface.co/spaces/haoheliu/audioldm-text-to-audio-generation/blob/main/ckpt/ldm_trimmed.ckpt, and place it under the `ckpt` folder.

4. Run the plugin:

```bash
python debug.py
```

5. Start TuneFlow Desktop and run the "Plugin Development" plugin.
