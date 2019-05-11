import subprocess, sys, requests
import json
from emission.net.int_service.machine_configs import controller_ip, controller_port, register_user_endpoint


controller_addr = "{}:{}".format (controller_ip, controller_port)
username = "test_analyst"

# Default location of the query.
query_file = "query.json"

def main (csv_file):
    r = requests.post (controller_addr + register_user_endpoint, json={'user':username})
    with open (query_file, "r") as f:
        query = json.load (f)
        print(query)
    if r.ok:
        subprocess.run (["python", "emission/net/ext_service/aggregator.py", controller_addr, "4", username, "test-querier", csv_file])

        # Put timer here, gets the time of launching the aggregator.
    else:
        print ("Error when registering the user.", file=sys.stderr)
        sys.exit (1)

if __name__ == "__main__":
    csv_file = sys.argv[1]
    main (csv_file)
