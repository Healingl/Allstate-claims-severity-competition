# coding=utf-8

from __future__ import print_function
def print(*arg):
	mystring = ""
	for argument in arg:
		mystring += str(argument)
	f = open('log.txt', 'a')
	f.write(mystring + "\n")
	f.close()

# Initialize SparkContext
import sys
from pyspark import SparkContext
from pyspark import SparkConf
sc = SparkContext()
import os
import sys
import re
from pyspark import SparkContext
from pyspark import SparkContext
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
from pyspark.sql import types
from pyspark.sql import Row
from pyspark.sql import functions
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd
import numpy as np
import pyspark.sql.functions as func
import matplotlib.patches as mpatches
import time as time
from matplotlib.patches import Rectangle
import datetime
import ast
from operator import add
import math
from itertools import combinations
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes
from pyspark.mllib.regression import LinearRegressionWithSGD
from pyspark.mllib.linalg.distributed import RowMatrix
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.ml import Pipeline
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.feature import VectorSlicer
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

df = sqlContext.createDataFrame(sc.pickleFile("rdd.p", 30), ["label", "features"]).cache()
