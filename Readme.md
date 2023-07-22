## Setup server requirements
    sudo apt update
    sudo apt install build-essential
    
## First make a env
    conda create -n "chatPDF"
 
## Install dependency 
    pip install --upgrade pip setuptools
    pip install -r requirement.txt

## Start the sever 
    uvicorn app:app --reload --port 8008

## Now Run in Postman
