from setuptools import setup, find_packages

setup(name="census-income",
	  version= "0.0.1" ,
	  author = "Pavan" ,
	  author_email = "pavankumar.chayanam@gmail.com" ,
	  package = find_packages(),
	  install_requirements=["pandas","numpy","flask"]
	 )
