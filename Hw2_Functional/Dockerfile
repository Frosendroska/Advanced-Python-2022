FROM python:3.9
COPY main.py main.py
COPY array.txt array.txt
RUN apt-get update
RUN apt-get install -y texlive graphviz graphviz-dev python3-pygraphviz
RUN pip install networkx
RUN pip install GeneratorOfFibAST==7.0
RUN python3.9 main.py array.txt
