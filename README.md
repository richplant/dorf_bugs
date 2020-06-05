# dorf_bugs
Create your own Dwarf Fortress bugs with machine learning

This is a little toy project designed to generate sample Dwarf Fortress bug texts using a pre-trained neural network. 
We'll be using Tensorflow 1.14 and the [GPT-2-simple](https://github.com/minimaxir/gpt-2-simple) package to do this in as few steps as possible.

## Installation
* clone the repo
* set up a config.py with your Twitter access token/api key etc
* STRONGLY RECOMMENDED set up a new env (you'll run into Tensorflow incomptabilities, trust me)
* pip install -r requirements.txt
* take a moment to get your [gpu sorted out](https://www.tensorflow.org/install/gpu)

## Usage
* run the Jupyter notebok to get started
* the send_msg.py file is set up to be run as a cron job

You can check out the results at https://twitter.com/DwarfBugs
