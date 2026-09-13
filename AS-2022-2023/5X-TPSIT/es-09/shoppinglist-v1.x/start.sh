#!/bin/bash
# file: start.sh

clear
rm -rf ./__pycache__	# remove old fastapi cache
PARAM="$1"				# append other params, example: --no-use-colors
# find your fastapi python starter file
for f in $(ls -1 | grep .py) do
	FILE="${f%.*}"
	break
done
APP=webapp
# set HOST=<YOUR_IP>
HOST=$(ip addr show | grep -w inet | awk '{print $2}' | cut -d '/' -f 1)
PORT=80						# set your default port
PYTHON=$(which python3)		# set your python path 

# *** upgrade outdated pyhon pip modules
function upgrade_python_modules {
	echo -e "\e[36mCheck and Update your outdated python pip modules...\e[0m"
	pip install --upgrade "$1"
}
# upgrade_python_modules $(pip list --outdated | awk '{print $1}')

# *** check and install missing Python pip modules ***
function check_modules {
	echo -e "\e[36mCheck your python pip modules...\e[0m"
	for i in "$1" do
		if ! $PYTHON -m pip show $i > /dev/null 2>&1;
		then
			echo -e "[\e[33m$i\e[0m] \e[31mNot found\e[0m, installing.."
			$PYTHON -m pip install $i
		else
			echo -e "[\e[33m$i\e[0m] \e[32malready\e[0m installed.."
		fi
	done
}
# check_modules "httptools uvicorn fastapi jinja2"

# run your favorite browser on your local ip address
xdg-open "http://$HOST:$PORT/" &

# run your FastAPI app
$PYTHON -m uvicorn $FILE:$APP --reload --host 0.0.0.0 --port $PORT --http httptools $PARAM
