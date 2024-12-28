down:
	python3 ./src/download.py
setup:
	python3 -m venv myenv && . myenv/bin/activate && pip3 install yt-dlp && python3 ./src/download.py