"""
nacos 官网
https://nacos.io/en-us/

本 SDK 基于 Open-API
https://nacos.io/en-us/docs/open-api.html
"""

name = "Pynacos"
class CreatNewNacos:
    def __init__(self, ip, port):
        from .NacosAdmin import NacosAdmin
        from .NacosConfig import NacosConfig
        from .NacosInstance import NacosInstance
        from .NacosService import NacosService
        from .HoldConfig import HoldConfig

        self.NacosAdmin = NacosAdmin(ip, port)
        self.NacosConfig = NacosConfig(ip, port)
        self.NacosInstance = NacosInstance(ip, port)
        self.NacosService = NacosService(ip, port)
        self.HoldConifg = HoldConfig(ip, port, self.NacosConfig)



