{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'train': [{'input': [[0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0],\n",
       "    [0, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 3, 0, 3, 0],\n",
       "    [0, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0],\n",
       "    [0, 3, 4, 3, 0, 0],\n",
       "    [0, 0, 3, 4, 3, 0],\n",
       "    [0, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0]]},\n",
       "  {'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 3, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0, 3, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 3, 3, 0, 0, 0],\n",
       "    [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 3, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0, 3, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 3, 4, 3, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 3, 3, 0, 0, 0],\n",
       "    [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]},\n",
       "  {'input': [[0, 0, 0, 0, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],\n",
       "    [0, 3, 3, 0, 3, 3, 0, 3, 0, 0],\n",
       "    [3, 0, 0, 3, 0, 0, 3, 0, 3, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 3, 0, 0, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 3, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],\n",
       "    [0, 3, 3, 0, 3, 3, 0, 3, 0, 0],\n",
       "    [3, 0, 0, 3, 4, 4, 3, 4, 3, 0],\n",
       "    [0, 0, 0, 3, 4, 4, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 3, 4, 4, 3, 0, 0, 0],\n",
       "    [0, 0, 0, 3, 4, 4, 3, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]},\n",
       "  {'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 3, 3, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 3, 3, 3, 3, 3, 3, 3, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 0, 3, 3, 0],\n",
       "    [0, 0, 0, 3, 3, 0, 0, 3, 0, 3],\n",
       "    [0, 0, 0, 3, 0, 3, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 3, 3, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 4, 4, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 4, 4, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 3, 3, 3, 3, 3, 3, 3, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 3, 0, 0, 0, 3, 3, 0],\n",
       "    [0, 0, 0, 3, 3, 0, 0, 3, 4, 3],\n",
       "    [0, 0, 0, 3, 4, 3, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]]},\n",
       "  {'input': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 3, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 3, 3, 3, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 3, 3, 4, 4, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 3, 3, 0, 0, 3, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 4, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}],\n",
       " 'test': [{'input': [[0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0,\n",
       "     0],\n",
       "    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],\n",
       "   'output': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 3, 4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 4, 4, 4, 4, 3, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 4, 4, 4, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 3, 4, 4, 4, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 3, 3, 4, 3, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0],\n",
       "    [0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 3, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],\n",
       "    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}]}"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import json\n",
    "data = json.load(open(\"/Users/saibhe.mccullough/Documents/College/Tools for AI/Assignment3/ARC/ARC/data/training/00d62c1b.json\"))\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['train', 'test'])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data['train'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'input': [[0, 0, 0, 0, 0, 0],\n",
       "  [0, 0, 3, 0, 0, 0],\n",
       "  [0, 3, 0, 3, 0, 0],\n",
       "  [0, 0, 3, 0, 3, 0],\n",
       "  [0, 0, 0, 3, 0, 0],\n",
       "  [0, 0, 0, 0, 0, 0]],\n",
       " 'output': [[0, 0, 0, 0, 0, 0],\n",
       "  [0, 0, 3, 0, 0, 0],\n",
       "  [0, 3, 4, 3, 0, 0],\n",
       "  [0, 0, 3, 4, 3, 0],\n",
       "  [0, 0, 0, 3, 0, 0],\n",
       "  [0, 0, 0, 0, 0, 0]]}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['train'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# iterate over rows of input\n",
    "#Check for pattern\n",
    "    #If true:\n",
    "       # add value 4 instead of 3\n",
    "    #If false:\n",
    "        #pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "#Access first input\n",
    "my_list = data['train'][0]['input']\n",
    "my_list\n",
    "\n",
    "my_list = np.array([my_list])\n",
    "\n",
    "\n",
    "\n",
    "#my_list[2][3]\n",
    "\n",
    "#print (my_list[1][2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "3\n",
      "rows 1\n",
      "item 2\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "3\n",
      "rows 2\n",
      "item 1\n",
      "0\n",
      "3\n",
      "rows 2\n",
      "item 1\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "3\n",
      "rows 3\n",
      "item 2\n",
      "0\n",
      "3\n",
      "rows 3\n",
      "item 2\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "3\n",
      "rows 4\n",
      "item 3\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "#get all the items that need to be analysed\n",
    "\n",
    "locations = []\n",
    "for row in my_list:\n",
    "  #  print (row)\n",
    "   # print ('row', type(row))\n",
    "    for item in row:\n",
    "        print(item)\n",
    "       # print ('item index', my_list.index(item))\n",
    "        if item != 0:\n",
    "         #   pass\n",
    "       # else:\n",
    "            print ('rows', my_list.index(row))   \n",
    "            print('item', row.index(item))\n",
    "            #location_index = my_list.index(row),row.index(item)\n",
    "            #locations.append(location_index)\n",
    "            #print (location_index)\n",
    "#print (locations)\n",
    "           # print (location_index)\n",
    "            #print (my_list.index(row), row.index(item))\n",
    "            #print ('here')\n",
    "            #for location_index in locations:\n",
    "\n",
    "#locations[3][1]\n",
    "#analyse the items for the pattern\n",
    "\n",
    "#for location_index in locations:\n",
    "   # print (location_index)\n",
    "            \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0, 0, 0, 0, 0, 0],\n",
       "        [0, 0, 3, 0, 0, 0],\n",
       "        [0, 3, 0, 3, 0, 0],\n",
       "        [0, 0, 3, 0, 3, 0],\n",
       "        [0, 0, 0, 3, 0, 0],\n",
       "        [0, 0, 0, 0, 0, 0]]])"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "result = np.where(my_list == 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 0, 0, 0, 0, 0]),\n",
       " array([1, 2, 2, 3, 3, 4]),\n",
       " array([2, 1, 3, 2, 4, 3]))"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tuple of arrays returned :  (array([0, 0, 0, 0, 0, 0]), array([1, 2, 2, 3, 3, 4]), array([2, 1, 3, 2, 4, 3]))\n"
     ]
    }
   ],
   "source": [
    "print('Tuple of arrays returned : ', result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [],
   "source": [
    "listOfCoordinates= list(zip(result[1], result[2]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3)]"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "#Access first input\n",
    "my_list = data['train'][0]['input']\n",
    "my_list\n",
    "\n",
    "my_list = np.array([my_list])\n",
    "result = np.where(my_list == 3)\n",
    "listOfCoordinates= list(zip(result[1], result[2]))\n",
    "listOfCoordinates\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3)]\n"
     ]
    }
   ],
   "source": [
    "print (listOfCoordinates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3)]"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listOfCoordinates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(listOfCoordinates[0][1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(listOfCoordinates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "current (1, 2)\n",
      "2\n",
      "1 2\n",
      "none found\n",
      "left (2, 1)\n",
      "right (2, 3)\n",
      "bottom (3, 2)\n",
      "(2, 1) (2, 3) (3, 2)\n",
      "right (3, 4)\n",
      "bottom (3, 2)\n",
      "(2, 1) (3, 4) (3, 2)\n",
      "right (4, 3)\n",
      "bottom (3, 2)\n",
      "(2, 1) (4, 3) (3, 2)\n",
      "none found\n",
      "none found\n",
      "none found\n"
     ]
    }
   ],
   "source": [
    "#i = 0\n",
    "#while i <=len(listOfCoordinates):\n",
    "current_coord = listOfCoordinates[0]\n",
    "    #next_coord = listOfCoordinates[i+1]\n",
    "print ('current', current_coord)\n",
    "    #print ('next', next_coord)\n",
    "    #pattern = current_cord[]\n",
    "current_coord\n",
    "#current_coord[0][0]\n",
    "#current_coord[0][0]\n",
    "listOfCoordinates[2][0] \n",
    "\n",
    "print(current_coord[1])\n",
    "x = current_coord[0]\n",
    "y = current_coord[1]\n",
    "print (x,y)\n",
    "\n",
    "for coord in listOfCoordinates:\n",
    "    current = coord\n",
    "    \n",
    "    #check for 3 in next row down, to the left\n",
    "    if coord[0] == (x+1): \n",
    "       # print ('x left')\n",
    "        if coord[1] < y:\n",
    "          #  print ('Y left')\n",
    "            print ('left', coord)\n",
    "            left = coord\n",
    "            \n",
    "            #check for 3 on this row, to the right\n",
    "            for coord in listOfCoordinates:\n",
    "                if coord[1] > y:\n",
    "                  #  print ('Y on the right also')\n",
    "                    print ('right', coord)\n",
    "                    right = coord\n",
    "                    for coord in listOfCoordinates:\n",
    "                        if coord[0] == (x+2):\n",
    "                            #print ('x on the bottom')\n",
    "                            if coord[1] == y:\n",
    "                               # print ('Y on the bottom also')\n",
    "                                print ('bottom', coord)\n",
    "                                bottom = coord\n",
    "                                print (left, right, bottom)\n",
    "                                \n",
    "                                #need to find all locations in between current, left, right, bottom, and fill them in with a number\n",
    "            \n",
    "            \n",
    "            \n",
    "        \n",
    "    else:\n",
    "        print ('none found')\n",
    "\n",
    "   # i +=1"
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
