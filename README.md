# 108_1 Data Structure and Algorithm
:::success
巨資三B：資料結構與演算法
吳宜璇 Yuni
:::

- [108_1 Data Structure and Algorithm](#108-1-data-structure-and-algorithm)
- [Leetcode](#leetcode)
- [Notes](#notes)
  * [__Linked List__](#--linked-list--)
    + [Learning](#learning)
      - [Intro](#intro)
      - [Linked List & Array](#linked-list---array)
    + [Reading](#reading)
    + [Additional](#additional)
  * [**Min Stack**](#--min-stack--)
    + [Learning](#learning-1)
      - [Intro](#intro-1)
    + [Reading](#reading-1)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



# Leetcode
  
   * [**WEEK2-Linked List**](https://github.com/Yuni-wih/DSA-learning/tree/master/DSA-Leetcode/Week2%20%7C%7C%20Linked%20List)

   * [**WEEK3-MinStack**](https://github.com/Yuni-wih/DSA-learning/tree/master/DSA-Leetcode/Week3%20%7C%7C%20MinStack)

   * [**WEEK4-Set Mismatch**](https://github.com/Yuni-wih/DSA-learning/tree/master/DSA-Leetcode/Week4%20%7C%7C%20Set%20Mismatch)
   * [**WEEK5-Quick Sort**]()


# Notes

## __Linked List__
* ### Learning

    * #### Intro
        * Linked-list是由一連串的節點`Node`所構成，每個節點指向下一個節點，而最後一個節點則指向None，因此，每個節點本身應該要有兩種`屬性`（attribute），一個是本身帶有的值或者是資料，另一個則是指向下一個節點的指標->（pointer）。
    ![](https://i.imgur.com/AOctXtZ.png)
    * #### Linked List & Array
        * Linked List屬於鏈式儲存結構，可以快速插入、刪除和移動，因此不會浪費太多記憶體的空間；Array是順序儲存結構，優點：無需為表中元素之間的邏輯關係而增加額外的儲存空間；可以快速的存取表中任一位置的元素缺點：插入和刪除操作需要移動大量元素；當線性表長度變化較大時，難以確定儲存空間的容量。
 
* ### Reading
    * [用python實作linked-list](https://medium.com/@tobby168/用python實作linked-list-524441133d4d)
    * [Linked List - 鏈表](https://algorithm.yuanbin.me/zh-tw/basics_data_structure/linked_list.html)
    * [Python 数据结构入门 - 链表（Linked List）](https://python123.io/index/topics/data_structure/linked_list)

* ### Additional
    * 時間複雜度：衡量演算法執行好壞的工具，不是以秒來計算，而是以步驟次數來計算。
        * 👉[Link](https://medium.com/appworks-school/初學者學演算法-從時間複雜度認識常見演算法-一-b46fece65ba5)

## **Min Stack**

* ### Learning

    * #### Intro
        * Stack是具有「Last-In-First-Out」的資料結構(可以想像成一種裝資料的容器)，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」。

        * Push(data)：把資料放進Stack。
          Pop：把「最上面」的資料從Stack中移除。
          Top：回傳「最上面」的資料，不影響資料結構本身。
          IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。
          getSize：回傳Stack裡的資料個數，不影響資料結構本身。

    ![](https://i.imgur.com/H3HBwef.png)
    
* ### Reading
    * [Stack: Intro(簡介)](http://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)



