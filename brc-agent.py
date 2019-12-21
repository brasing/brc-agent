#! /usr/bin/env python

import falcon
import libvirt

class ThingsResource(object):
    def on_get(self, req, resp):
        responseStatus = falcon.HTTP_500
        responseBody = 'Something went horribly wrong'

        print('Connecting to libvirt')
        conn = libvirt.open('qemu:///system')
        if conn == None:
            responseBody = 'Failed to open connection to the hypervisor'
        print(conn)

        numberOfDomains = None
        try:
            responseBody = 'There are %d domains running' % (conn.numOfDomains()) 
            print(responseBody)
            responseStatus = falcon.HTTP_200
        except:
            responseBody = 'Failed to get the number of running domains'

        resp.status = responseStatus
        resp.body = ('\n' + responseBody + '\n')

app = falcon.API()

things = ThingsResource()

app.add_route('/things', things)
