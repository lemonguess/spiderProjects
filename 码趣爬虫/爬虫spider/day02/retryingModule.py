from retrying import retry

# @retry# 如出现异常会一直重试
# @retry(stop_max_attempt_number=3)  # 用来设定最大的尝试次数，超过该次数就停止重试
# @retry(stop_max_delay=3000)  # 设置失败重试的最大时间, 单位毫秒，超出时间，则停止重试  3秒之后报错
# @retry(wait_fixed=2000)  # 设置失败重试的间隔时间
@retry(wait_random_min=1000, wait_random_max=5000, stop_max_attempt_number=3)  # 设置失败重试随机性间隔时间  有时块，有时慢
def demo():
    print("--------")
    raise

demo()