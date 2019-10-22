import Pynacos

print(Pynacos.name)

pynacos = Pynacos.CreatNewNacos(
    ip = "ip",
    ip = "a.martin98.top",
    port = 8848
)
pynacos.HoldConifg.Start("test", "test", contentMD5="", target=print)
config = pynacos.NacosConfig.Get("test", "test")
print(config)