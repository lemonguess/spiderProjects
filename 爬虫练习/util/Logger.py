import logging

#设置输出样式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s [%(filename)s:%(lineno)d]: %(message)s',#输出格式
    filename='log.log',
    filemode='w'
)
logger = logging.getLogger(__name__)