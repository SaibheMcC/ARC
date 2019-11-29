{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "train [[0, 2, 0], [2, 2, 0], [0, 2, 0], [0, 2, 1], [0, 2, 0], [2, 2, 0], [0, 2, 1], [0, 2, 0], [2, 2, 0]]\n",
      "train [[0, 2, 0], [2, 0, 1], [0, 2, 0], [2, 0, 1], [0, 2, 0], [2, 0, 1], [2, 0, 1], [0, 2, 0], [2, 0, 1]]\n",
      "train [[0, 2, 0], [2, 2, 0], [0, 2, 0], [0, 2, 0], [2, 2, 0], [0, 2, 0], [0, 2, 0], [2, 2, 0], [0, 2, 0]]\n",
      "test [[1, 2, 2], [0, 2, 0], [0, 2, 0], [1, 2, 2], [0, 2, 0], [0, 2, 0], [1, 2, 2], [0, 2, 0], [0, 2, 0]]\n"
     ]
    }
   ],
   "source": [
    "import json #import the json library\n",
    "\n",
    "def solve():\n",
    "\n",
    "    d = json.load(open(\"/Users/saibhe.mccullough/Documents/College/Tools for AI/Assignment3/ARC/ARC/data/training/017c7c7b.json\"))\n",
    "\n",
    "    # list of set values (train set or test set)\n",
    "    set_values = ['train', 'test']\n",
    "\n",
    "    #iterate over each value in set_values\n",
    "    for value in set_values:\n",
    "\n",
    "        #while the count is less than the length of the set (training set or test set)\n",
    "        i = 0\n",
    "        count = len(d[value])\n",
    "        while i < count:\n",
    "\n",
    "            #access input i of each set\n",
    "            input = d[value][i]['input']\n",
    "\n",
    "            #iterate over input values\n",
    "            #change values of 1's to 2's\n",
    "            for row in input:\n",
    "                for column in row:\n",
    "                    if row[column] == 1:\n",
    "                        row[column] = 2\n",
    "            \n",
    "            #get second half of data and append it onto the end of the data (this needs to be more specific - and capture 3 rows, but not the last row)\n",
    "            sub_list = input[int(len(input)/2):]\n",
    "\n",
    "            for x in sub_list:\n",
    "                input.append(x)\n",
    "            print (value, input)    \n",
    "        \n",
    "            i+=1 \n",
    "            \n",
    "solve()            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(input[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "input[0] = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5,\n",
       " [0, 2, 0],\n",
       " [0, 2, 0],\n",
       " [1, 2, 2],\n",
       " [0, 2, 0],\n",
       " [0, 2, 0],\n",
       " [1, 2, 2],\n",
       " [0, 2, 0],\n",
       " [0, 2, 0]]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input"
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
