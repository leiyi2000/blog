import time

import httpx
import pytest
import multiprocessing

from granian import Granian
from granian.constants import Interfaces


def run_server():
    """在单独的进程中运行服务器"""
    server = Granian('blog.asgi:application', address='0.0.0.0', port=7788, interface=Interfaces.ASGI)
    server.serve()


@pytest.fixture(scope="session")
def asgi_app():
    print("启动 Granian 服务器...")
    # 创建服务器进程，不设置daemon=True
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()
    print("Granian 服务器已启动")
    time.sleep(2)
    yield
    # 测试结束后关闭服务器进程
    server_process.terminate()
    server_process.join(timeout=5)
    print("Granian 服务器已关闭")


@pytest.mark.asyncio
async def test_read(asgi_app):
    """测试访问文章详情页"""
    print("开始测试文章访问...")
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://127.0.0.1:7788/article/1")
        assert resp.status_code == 200
        print(resp.json())
