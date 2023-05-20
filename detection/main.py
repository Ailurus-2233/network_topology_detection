from fastapi import FastAPI
import json
from utils import traceroute, capture
from models.traceroute import Traceroute
from models.capture import Capture
import scapy.all as sca


app = FastAPI(title="detection Node", version="1.0")


@app.get("/")
def root():
    return {
        "节点名称": "detection",
        "API": ["/capture", "/traceroute"],
        "说明": ["用于开始捕获当前节点的流量数据，并将IP地址提交到核心节点", "用于对指定IP地址进行路由跟踪，并将结果提交到核心节点"],
    }


@app.get("/capture")
def capture():
    with open("config.json", "r") as f:
        config = json.load(f)
    ans = capture.catch_packet(
        iface=config["iface"],
        count=config["count"],
        timeout=config["timeout"],
        filter=config["filter"],
    )
    return ans


@app.post("/capture")
def capture(capture: Capture):
    ans = capture.catch_packet(
        iface=capture.iface,
        count=capture.count,
        timeout=capture.timeout,
        filter=capture.filter,
    )
    return ans


@app.get("/get_iface")
def get_iface():
    iface_list = sca.get_if_list()
    ans = []
    for iface in iface_list:
        ans.append(sca.conf.ifaces.__dict__["data"][iface].name)
    return ans


@app.post("/get_traceroute")
def get_traceroute(info: Traceroute):
    print(info)
    return traceroute.get_traceroute(info.host, info.timeout, info.maxttl)
