# VistA Self Hosted AI

An MCP server that integrates with a self hosted Ollama container and returns information related to VistA patients.

# Pre-requisites

1) [Docker](https://docs.docker.com/engine/install/)
2) [docker-compose](https://docs.docker.com/compose/install/linux/)

# To run:

     git clone https://github.com/RamSailopal/VistAAI.git
     cd VistAAI
     docker-compose up -d
     
This will run a number of containers:

1) An ollama container
2) A "side car" container that will pull the llama3.2 model into ollama
3) A VistA container along with fmQL (Fileman query language)
4) An mcp-server

You will need to wait for the containers to fully initialise before things can proceed and so monitor them with:

     docker-compose logs -f 

Once all the containers have initialised and there is no further output on the screen, press Ctrl+C. You can now access the AI mcp-server console via:

     ./mcp-server.sh

You now begin to ask questions about VistA.

# Programmed VistA context

## Drugs

![VistA Drug list](/Images/Vista_drug_list.png "VistA Drug List")

![VistA Drug Details](/Images/Vista_drug_det.png "VistA Drug Details")

![General Drug Information](/Images/drug_gen_info.png "General Drug informtion")

## Patients

![VistA Patient list](/Images/Vista_pat_list.png "VistA Patient List")

![VistA Patient Details](/Images/vista_pat_det.png "VistA Patient Details")

The AI model is intellegent enough to know that the details returned have confidentials/sensitive information and refuses.

# Ollama WebUI

In additional an Ollama web UI container runs. This container references the Ollama llama 3.2 model without an mcp server and no interaction with Vista. The web UI can be accessed via the web address:

http://localhost:8001

**NOTE** - This is a self hosted AI and the speed of the responses will be dependant on the hardware on which the AI model is running.

# Functionality

The Python code **mcp/vista.py** provides the context about VistA to the AI model. When writing the code, Python function docstrings/comments are important with regards to helping the AI model understand the context.

# Further Information:

[Ollama docker container](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)
[mcp-host](https://github.com/mark3labs/mcphost)
[VistA](https://worldvista.org/)
[fmQL](https://github.com/borochris/FMQL)