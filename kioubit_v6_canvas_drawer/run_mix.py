import json,socket
import concurrent.futures
import subprocess,asyncio
import struct,sys
from typing import Optional, Tuple

threads = int(sys.argv[1])  # 綫程數
hosts_file = sys.argv[2]  # 存储IP地址的JSON文件路径

ICMP_ECHO = 8

def icmpv6_bare_request(target: str, source_address: Optional[str] = None) -> None:
    """
    Send a bare icmpv6 request.

    Args:
        - `target` (`str`): the target the packet sent to
        - `source_address` (`Optional[str]`): the source address used to send packet if set (default: `None`)
    """

    header = struct.pack(
        "!BBHHH", ICMP_ECHO, 0, 0, 0, 0
    )

    sock = socket.socket(socket.AF_INET6, socket.SOCK_RAW, socket.IPPROTO_ICMPV6)

    if source_address:
        sock.bind((source_address, 1))
    sock.sendto(header, (target, 0, 0, 0))
    sock.close()



async def sping(ip):
    #print(f"Ping {ip}")
    icmpv6_bare_request(ip, 'fd42:1877:222c::ba:1')
    

async def ping_all(ips):
    tasks = []
    
    print (f'task running')
    
    for ip in ips:
        tasks.append(asyncio.create_task(sping('fdcf:8538:9ad5:3333:' + ip)))
    
    await asyncio.gather(*tasks)

def aping(ips):
    asyncio.run(ping_all(ips))
    
    #for ip in ips:
    #    print(ip + '\n')
    #    asyncio.run(subprocess.Popen(["ping", "-w", "0", "-c", "1", ip],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))

if __name__ == '__main__':
    with open(hosts_file, "r") as f:
        ips = json.load(f)            
    
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        
            # 计算线程池中的线程数
            num_threads = executor._max_workers

            # 计算每个线程要处理的元素数
            chunk_size = len(ips) // num_threads
            #chunk_size = 200

            # 将数组分成块，每个块包含 chunk_size 个元素
            array_chunks = [ips[i:i + chunk_size] for i in range(0, len(ips), chunk_size)]
            
            # 将每个块提交给线程池中的一个线程进行处理
            futures = [executor.submit(aping, element) for element in array_chunks]



        # 等待所有任务完成
        concurrent.futures.wait(futures)
