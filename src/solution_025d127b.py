{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'train': [{'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 6, 6, 6, 0, 0, 0, 0, 0],\n",
       "    [0, 6, 0, 0, 6, 0, 0, 0, 0],\n",
       "    [0, 0, 6, 0, 0, 6, 0, 0, 0],\n",
       "    [0, 0, 0, 6, 0, 0, 6, 0, 0],\n",
       "    [0, 0, 0, 0, 6, 6, 6, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 2, 2, 2, 0, 0, 0, 0],\n",
       "    [0, 0, 2, 0, 0, 2, 0, 0, 0],\n",
       "    [0, 0, 0, 2, 2, 2, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 6, 6, 6, 0, 0, 0, 0],\n",
       "    [0, 0, 6, 0, 0, 6, 0, 0, 0],\n",
       "    [0, 0, 0, 6, 0, 0, 6, 0, 0],\n",
       "    [0, 0, 0, 0, 6, 0, 6, 0, 0],\n",
       "    [0, 0, 0, 0, 6, 6, 6, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 2, 2, 2, 2, 0, 0],\n",
       "    [0, 0, 0, 2, 0, 0, 2, 0, 0],\n",
       "    [0, 0, 0, 2, 2, 2, 2, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0]]},\n",
       "  {'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 8, 8, 8, 8, 8, 0, 0, 0],\n",
       "    [0, 8, 0, 0, 0, 0, 8, 0, 0],\n",
       "    [0, 0, 8, 0, 0, 0, 0, 8, 0],\n",
       "    [0, 0, 0, 8, 0, 0, 0, 0, 8],\n",
       "    [0, 0, 0, 0, 8, 8, 8, 8, 8],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 8, 8, 8, 8, 8, 0, 0],\n",
       "    [0, 0, 8, 0, 0, 0, 0, 8, 0],\n",
       "    [0, 0, 0, 8, 0, 0, 0, 0, 8],\n",
       "    [0, 0, 0, 0, 8, 0, 0, 0, 8],\n",
       "    [0, 0, 0, 0, 8, 8, 8, 8, 8],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0]]}],\n",
       " 'test': [{'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 4, 4, 4, 4, 4, 4, 0, 0, 0],\n",
       "    [0, 4, 0, 0, 0, 0, 0, 4, 0, 0],\n",
       "    [0, 0, 4, 0, 0, 0, 0, 0, 4, 0],\n",
       "    [0, 0, 0, 4, 0, 0, 0, 0, 0, 4],\n",
       "    [0, 0, 0, 0, 4, 4, 4, 4, 4, 4],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 4, 4, 4, 4, 4, 4, 0, 0],\n",
       "    [0, 0, 4, 0, 0, 0, 0, 0, 4, 0],\n",
       "    [0, 0, 0, 4, 0, 0, 0, 0, 0, 4],\n",
       "    [0, 0, 0, 0, 4, 0, 0, 0, 0, 4],\n",
       "    [0, 0, 0, 0, 4, 4, 4, 4, 4, 4],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}]}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import json\n",
    "data = json.load(open(\"/Users/saibhe.mccullough/Documents/College/Tools for AI/Assignment3/ARC/ARC/data/training/025d127b.json\"))\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(data['train'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['train'][0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 2 train [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 6, 6, 6, 0, 0, 0, 0, 0], [0, 6, 0, 0, 6, 0, 0, 0, 0], [0, 0, 6, 0, 0, 6, 0, 0, 0], [0, 0, 0, 6, 0, 0, 6, 0, 0], [0, 0, 0, 0, 6, 6, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 0, 0, 0, 0], [0, 0, 2, 0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 2, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]\n",
      "14\n",
      "[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 6, 6, 0, 0, 0, 0], [0, 6, 0, 0, 6, 0, 0, 0, 0], [0, 0, 6, 0, 0, 6, 0, 0, 0], [0, 0, 0, 6, 0, 0, 6, 0, 0], [0, 0, 0, 0, 6, 6, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 0, 0, 0, 0], [0, 0, 2, 0, 0, 2, 0, 0, 0], [0, 0, 0, 2, 2, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]\n",
      "1 2 train [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 8, 8, 8, 8, 8, 0, 0, 0], [0, 8, 0, 0, 0, 0, 8, 0, 0], [0, 0, 8, 0, 0, 0, 0, 8, 0], [0, 0, 0, 8, 0, 0, 0, 0, 8], [0, 0, 0, 0, 8, 8, 8, 8, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]\n",
      "8\n",
      "[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 8, 8, 8, 8, 8, 0, 0], [0, 8, 0, 0, 0, 0, 8, 0, 0], [0, 0, 8, 0, 0, 0, 0, 8, 0], [0, 0, 0, 8, 0, 0, 0, 0, 8], [0, 0, 0, 0, 8, 8, 8, 8, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]\n",
      "0 1 test [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 4, 4, 4, 4, 4, 0, 0, 0], [0, 4, 0, 0, 0, 0, 0, 4, 0, 0], [0, 0, 4, 0, 0, 0, 0, 0, 4, 0], [0, 0, 0, 4, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]\n",
      "10\n",
      "[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4, 4, 4, 0, 0], [0, 4, 0, 0, 0, 0, 0, 4, 0, 0], [0, 0, 4, 0, 0, 0, 0, 0, 4, 0], [0, 0, 0, 4, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "data = json.load(open(\"/Users/saibhe.mccullough/Documents/College/Tools for AI/Assignment3/ARC/ARC/data/training/025d127b.json\"))\n",
    "data\n",
    "\n",
    "set_values = ['train', 'test']\n",
    "\n",
    "for value in set_values:\n",
    "\n",
    "#iterate over set\n",
    "    i= 0\n",
    "    count = len(data[value])\n",
    "    #print (count)\n",
    "    while i < count:\n",
    "\n",
    "    #Access first input\n",
    "        my_list = data[value][i]['input']\n",
    "        print (i, count, value, my_list)\n",
    "        \n",
    "        #insert 0 at element 0\n",
    "        my_list[1].insert(0, 0)\n",
    "        #remove last index\n",
    "        del my_list[1][-1]\n",
    "        \n",
    "        if len(my_list) > 10:\n",
    "            sub_list = my_list[-1]\n",
    "            #insert sub_list\n",
    "            my_list.insert(6, sub_list)\n",
    "            #remove last row\n",
    "            del my_list[-1]\n",
    "\n",
    "            sub_list = my_list[-1]\n",
    "            my_list.insert(6, sub_list)\n",
    "            del my_list[-1]\n",
    "            \n",
    "            \n",
    "        print (len(my_list))\n",
    "        print(my_list)\n",
    "        i +=1\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-2b027a5918da>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'train'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "type(data['train'][0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data['train'][0].keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(data['train'][0]['output'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list = data['train'][0]['input']\n",
    "my_list\n",
    "#list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list[1].insert(0, 0)\n",
    "del my_list[1][-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(my_list[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "del my_list[1][-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " my_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "index = 0\n",
    "while index < len(my_list):\n",
    "    for row in my_list:\n",
    "   # for item in row\n",
    "        my_list[index].insert(0, 0)\n",
    "        del my_list[index][-1]\n",
    "        print (row)\n",
    "        index +=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list[12:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sub_list = my_list[-1]\n",
    "sub_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sub_list[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list.insert(6, sub_list)\n",
    "del my_list[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list.insert(6, sub_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "del my_list[15:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       " [0, 8, 8, 8, 8, 8, 0, 0, 0],\n",
       " [0, 8, 0, 0, 0, 0, 8, 0, 0],\n",
       " [0, 0, 8, 0, 0, 0, 0, 8, 0],\n",
       " [0, 0, 0, 8, 0, 0, 0, 0, 8],\n",
       " [0, 0, 0, 0, 8, 8, 8, 8, 8],\n",
       " [0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       " [0, 0, 0, 0, 0, 0, 0, 0, 0]]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['train'][1]['input']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(data['train'][0]['input'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
