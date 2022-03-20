# 导包
import logging.handlers


# 获取日志器
# 使用单例模式封装
class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()

            # 设置日志器级别(总入口:什么级别的信息可以进来)
            cls.logger.setLevel(logging.INFO)
            # 获取控制台处理器
            sh = logging.StreamHandler()
            # 获取文件-以使时间分隔 处理器
            # 需要改变的只有文件路径参数,传参即可
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/log02.log",
                                                           # 凌晨 23.59.59 -> 第二天 23.59.59,一天一夜
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           # 处理器控制写入,设置写入文件格式的编码
                                                           encoding="utf-8"
                                                           )

            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(funcName)s:%(lineno)d)]-%(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到处理器 文件
            th.setFormatter(fm)
            # 将处理器 添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger


# logger.info("info 信息")
if __name__ == '__main__':
    # logger.info("info 信息")
    logger = GetLogger().get_logger()
    logger.info("infor message")
