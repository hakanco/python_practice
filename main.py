import sys
import logging

if __name__ == '__main__':
    logging.basicConfig(filename="problem.log", level=logging.DEBUG)
    logger = logging.getLogger()
    my_list = [2, 4, 6]
    try:
        x = 1/0
        for i in range(5):
            print(my_list[i])
    except IndexError as ie:
        print(ie)
        print("index error.")
        logger.error(ie)
    except Exception as e:
        print(e)
        print("something happened.")
        logger.error(e)
    else:
        logger.info("everything is ok!")
    finally:
        logger.info("application finished.")

    print("more code here.")

