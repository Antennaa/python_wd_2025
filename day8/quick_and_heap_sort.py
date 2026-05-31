# 作者: Antenna
# 2026年05月30日15时18分06秒
# Antenna2000@163.com
import random
import time

class Sort:
    def __init__(self,n):
        """
        :param n: 被排序数的数量
        """
        self.length = n
        self.array = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.length):
            self.array[i] = random.randint(0,99999)


    def partition(self,left,right):
        """
        分割函数
        :param left:左边界
        :param right:有边界
        :return: pivot
        """
        k = i = left # k 始终指向比分割值小的数要放置的位置的下标
        for i in range(left,right):
            if self.array[i] <= self.array[right]: #某个位置的值小于分隔值，将他与k所指的值交换
                self.array[i],self.array[k] = self.array[k],self.array[i]
                k += 1
        self.array[k], self.array[right] = self.array[right], self.array[k]
        return k

    def quick_sort(self,left,right):
        """
        快速排序
        :param left: 左边界
        :param right: 右边界
        :return: None
        """
        if left < right:
            pivot = self.partition(left,right) #分隔值的下标
            self.quick_sort(left,pivot-1)
            self.quick_sort(pivot+1,right)


    def adjust_max_heap(self,adjust_pos,arr_length):
        """
        把某个子树调整为大根堆
        :param adjust_pos:被调整的元素位置
        :param arr_length:当前列表总长度
        :return:None
        """
        parent = adjust_pos
        child = 2 * parent + 1 #左孩子和父亲的下标位置关系
        while child < arr_length: #下标要小于列表的长度
            #判断右孩子存在，且右孩子大于左孩子
            if child + 1 < arr_length and self.array[child] < self.array[child+1]:
                child += 1
            if self.array[child] > self.array[parent]:
                self.array[parent], self.array[child] = self.array[child], self.array[parent]
                parent = child
                child = 2 * parent + 1
            else:
                break


    def heap_sort(self):
        """
        堆排序
        :return: None
        """
        for i in range(self.length//2,-1,-1): #把列表调整为大根堆
            self.adjust_max_heap(i,self.length)
        #交换堆顶元素和最后一个元素
        self.array[0],self.array[self.length-1] = self.array[self.length-1],self.array[0]
        #不断控制无序数的总长度
        for i in range(self.length-1,1,-1):
            self.adjust_max_heap(0,i)
            self.array[0],self.array[i-1] = self.array[i-1],self.array[0]


    def test_time_use(self,sort_func,*args,**kwargs):
        """
        回调函数
        :param sort_func: 被调函数
        :param args:
        :param kwargs:
        :return: None
        """
        start = time.time()
        sort_func(*args,**kwargs)
        end = time.time()
        print(f'总计用时{end - start}s')


if __name__ == '__main__':
    my_sort = Sort(1000000)
    # print(my_sort.array)
    # my_sort.quick_sort(0,my_sort.length-1)
    # my_sort.heap_sort()
    my_sort.test_time_use(my_sort.quick_sort,0,my_sort.length-1)
    # print(my_sort.array)