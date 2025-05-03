from mcp.server.fastmcp import FastMCP
import requests

# Create an MCP server
mcp = FastMCP("Tell me about Vista test patients")

@mcp.tool()
def vista_pat_ids() -> str:
    """
    List all Vista test patients by ID.

    Args:

    Returns:
        str: Test patients IDs.
    """
    response = requests.get('http://fileman:9000/fmqlEP?fmql=DESCRIBE%202', timeout=30)
    data = response.json()
    pats="Patient IDs:\n\n"
    for pat in data["results"]:
        pats=pats + str(pat["social_security_number"]["value"]) + "\n"

    return pats

@mcp.tool()
def vista_pat_names() -> str:
    """
    List all Vista test patients by name.

    Args:

    Returns:
        str: Test patients namess.
    """
    response = requests.get('http://fileman:9000/fmqlEP?fmql=DESCRIBE%202', timeout=30)
    data = response.json()
    pats="Patient names:\n\n"
    for pat in data["results"]:
        pats=pats + str(pat["name"]["value"]) + "\n"

    return pats

@mcp.tool()
def vista_pat_details_name(name: str) -> str:
    """
    Tell me about a specific Vista test patient's details using name.

    Args:
        str: Test patient's name

    Returns:
        str: Test patient's details.
    """
    response = requests.get('http://fileman:9000/fmqlEP?fmql=DESCRIBE 2 FILTER (.01=' + name + ')', timeout=30)
    data = response.json()
    pats=[]
    for pat in data["results"]:
        pats.append("Name: " + str(pat["name"]["value"]) + "\nSex: " + str(pat["sex"]["value"]) + "\nDob: " + str(pat["date_of_birth"]["value"])
        + "\nBirth City: " + str(pat["place_of_birth_city"]["value"]) + "\nBirth State: " + str(pat["place_of_birth_state"]["sameAsLabel"]))

    return str(pats[0])

@mcp.tool()
def vista_pat_details_id(id: str) -> str:
    """
    Tell me about a specific Vista test patient's details using ID.

    Args:
        str: Test patient's ID

    Returns:
        str: Test patient's details.
    """
    response = requests.get('http://fileman:9000/fmqlEP?fmql=DESCRIBE 2 FILTER (.09=' + id + ')', timeout=30)
    data = response.json()
    pats=[]
    for pat in data["results"]:
        pats.append("Name: " + str(pat["name"]["value"]) + "\nSex: " + str(pat["sex"]["value"]) + "\nDob: " + str(pat["date_of_birth"]["value"])
        + "\nSSN: " + str(pat["social_security_number"]["value"]) + "\nBirth City: " + str(pat["place_of_birth_city"]["value"]) + "\nBirth State: " + str(pat["place_of_birth_state"]["sameAsLabel"]))

    return str(pats[0])

@mcp.tool()
def vista_drug_ord() -> str:
    """
    List all orderable drugs from pharmacy.

    Args:

    Returns:
        str: List of drugs.
    """
    response = requests.get('http://fileman:9000/fmqlEP?fmql=DESCRIBE%2050_7', timeout=30)
    data = response.json()
    drugs="Drugs:\n\n"
    for drug in data["results"]:
        drugs=drugs + str(drug["name"]["value"]) + "\n"

    return drugs

@mcp.tool()
def vista_drug_details(drug: str) -> str:
    """
    Tell me about a specific Vista drug details.

    Args:
        str: drug name

    Returns:
        str: Drug details.
    """
    response = requests.get('http://fileman:9000/fmqlEP?fmql=DESCRIBE 50_7 FILTER (.01=' + drug + ')', timeout=30)
    data = response.json()
    drugs=[]
    for drug in data["results"]:
        drugs.append("Dosage schedule: " + str(drug["schedule"]["value"]) + "\nMedical route: " + str(drug["default_med_route"]["label"]))

    return str(drugs[0])






