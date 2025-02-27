.. _operation

###############
Basic Operation
###############

Goal
====
    * 개별 Pixcel에 접근하고, 수정할 수 있다.
    * 이미지의 기본 속성을 확인 할 수 있다.
    * 이미지의 ROI(Region of Image)를 설정할 수 있다.
    * 이미지를 분리하고, 합칠 수 있다.

Pixel Value
===========

일반적으로 이미지를 Load하면 3차원 행렬형태로 생성이 됩니다. (100,300,3) 이러한 형태로 (행, 열, 색정보)를 의미합니다.

>>> import cv2
>>> import numpy as np

>>> img = cv2.imread('lena.jpg')

위와 같이 Load후에 특정 pixel을 값에 접근을 하려면 아래와 같이 접근할 수 있습니다.

>>> px = img[100,200]
>>> print px
[157 100 190]

즉, 100(행), 200(열)을 색값이 157(B), 100(G), 190(R) 인 것을 확인 할 수 있습니다.
만일 Blue값만을 확인하고 싶을 경우에는 아래와 같이 입력합니다.

>>> b = img[100,200,0]
>>> print b
157

세번째 Array값 중 0번째는 Blue, 1번째는 Green, 2번째는 Red를 의미합니다.
위와 같은 방법으로 특정 pixel의 값을 변경할 수도 있습니다.

>>> img[100,200] = [255, 255, 255]

위와 같이 입력을 하면 100,200의 색 값을 흰색으로 변경할 수 있습니다.

일반적으로 특정 Pixel값을 변경하기 위해서는 아래와 같이 사용합니다.(Numpy 사용 방법)

>>> img.item(10,10,2) # Red값
59

>>> img.itemset((10,10,2), 100) #Red값을 100으로 변경
>>> img.item(10,10,2)
100

이미지의 기본 속성
==================

이미지를 Load한 후에 해당 이미지의 기본적인 정보를 확인해야 합니다. 행과 열의 갯수가 몇개인지, 몇개의 Channel로
구성이되어 있는지가 기본입니다.
이를 확인하기 위해서 ``img.shape`` 를 사용하면 tuple형태로 (행, 열, channel) 정보를 Return합니다.


>>> img.shape
(206, 207, 3)

.. note:: 이미지가 Grayscale의 경우에는 행과 열만 Return이 됩니다.

전체 pixcel수의 확인은 ``img.size`` 로 확인이 가능합니다.

>>> img.size
42642

이미지의 Datatype은 ``img.dtype`` 으로 확인이 가능합니다.

>>> img.dtype
dtype('uint8')


이미지 ROI
==========

이미지 작업시에는 특정 pixel단위 보다는 특정 영역단위로 작업을 하게 됩니다. 이것을 Region of Image(ROI)라고 합니다.
ROI 설정은 Numpy의 indexing방법을 사용합니다. 만일 아래와 같이 특정 영역에 어떤 물체가 있다는 것을 알고 있으면
그 영역을 설정해서 Copy를 할 수도 있습니다.

>>> img = cv2.imread('baseball-player.jpg')
>>> ball = img[409:454, 817:884] # img[행의 시작점: 행의 끝점, 열의 시작점: 열의 끝점]
>>> img[470:515,817:884] = ball # 동일 영역에 Copy
>>> cv2.imshow('img', img)
>>> cv2.waitKey(0)
>>> cv2.destroyAllWindows()

.. figure:: ../../_static/06.basicOperation/1.jpg
    :align: center

    Original

.. figure:: ../../_static/06.basicOperation/2.jpg
    :align: center

    Result


이미지 crop
=========

이미지 ROI를 새로운 파일로 저장하여 이미지를 crop할 수 있습니다.

>>> img = cv2.imread('baseball-player.jpg')
>>> ball = img[409:454, 817:884] # img[행의 시작점: 행의 끝점, 열의 시작점: 열의 끝점]
>>> cv2.imwrite('ball.jpg', ball)


이미지 Channels
===============

Color Image는 3개의 채널 B,G,R로 구성이 되어 있습니다. 이것을 각 채널별로 분리할 수 있습니다.

>>> b, g, r= cv2.split(img)
>>> img = cv2.merge((r,g,b))

또는 Numpy indexing 접근 방법으로 표현할 수도 있습니다

>>> b = img[:,:,0] # 0 : Blue, 1 : Green, 2 : Red

.. warning:: ``cv2.split()`` 함수는 비용이 많이 드는 함수입니다. 가능하다면 Numpy indexing방법을 사용하는 효율적입니다.

특정 Channel의 값을 변경하려면 아래와 같이 입력합니다.

>>> img[:,:,2] = 0 #Red Channel을 0으로 변경. Red 제거하는 효과.

