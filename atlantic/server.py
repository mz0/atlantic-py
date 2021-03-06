from .utils import AtlanticBase

class AtlanticServer(AtlanticBase):
    def __init__(self, access_key, private_key):
        AtlanticBase.__init__(self, access_key, private_key)

    def run(self, servername, imageid, planname, vm_location,
            enablebackup="N", serverqty=1, cloneimage=None, key_id=None):
        """
        Create and run a new cloud server.

        Link: https://www.atlantic.net/docs/api/?shell#run-instance
        """
        params = {
            "Action": "run-instance",
            "servername": servername,
            "imageid": imageid,
            "planname": planname,
            "vm_location": vm_location,
            "enablebackup": enablebackup,
            "serverqty": serverqty
        }
        if cloneimage:
            params.update({"cloneimage": cloneimage})
        if key_id:
            params.update({"key_id": key_id})
        return self.request(params)

    def list(self):
        """
        List my cloud servers.

        Link: https://www.atlantic.net/docs/api/?shell#list-instances
        """
        params = {
            "Action": "list-instances"
        }
        return self.request(params)

    def describe(self, instanceid):
        """
        Get details of a cloud cerver.

        Link: https://www.atlantic.net/docs/api/?shell#describe-instance
        """
        params = {
            "Action": "describe-instance",
            "instanceid": instanceid
        }
        return self.request(params)

    def reboot(self, instanceid, reboottype="soft"):
        """
        Restart a cloud server.

        Link: https://www.atlantic.net/docs/api/?shell#reboot-instance
        """
        params = {
            "Action": "reboot-instance",
            "instanceid": instanceid,
            "reboottype": reboottype
        }
        return self.request(params)

    def terminate(self, instanceid):
        """
        Termianate a cloud server.

        Link: https://www.atlantic.net/docs/api/?shell#terminate-instance
        """
        params = {
            "Action": "terminate-instance",
            "instanceid": instanceid
        }
        return self.request(params)
