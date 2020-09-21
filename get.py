from REST import dnac


def help_me():
    return "I can help. Below are the commands that I understand:\n" \
           "`Help` - I will display what I can do. \n" \
           "`Status` - I will display your DNAC Status \n"
    
def network_health():
    nh = dnac.get_request('/dna/intent/api/v1/network-health')
    nht = nh['response'].pop()
    gresponse_total = f'You have a total of {nht["totalCount"]} devices, with a {nht["healthScore"]}% of health \n'
    nha = nh['healthDistirubution'][0] 
    gresponse_access = f'You have a total of {nha["totalCount"]} access switches, with a {nha["healthScore"]}% of health \n'
    nhd = nh['healthDistirubution'][1] 
    gresponse_distribution = f'You have a total of {nhd["totalCount"]} distribution switches, with a {nhd["healthScore"]}% of health \n'
    nhr = nh['healthDistirubution'][2] 
    gresponse_router = f'You have a total of {nhr["totalCount"]} routers, with a {nhr["healthScore"]}% of health'

