
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h2>The Institute for Ethical AI & ML</h2>
<h3>The state of MLOps in 2019</h3>
<p>
  <br />
  <br />
    Alejandro Saucedo | <a href="">a@ethical.institute</a><br/><br/>
    Twitter: <a href="http://twitter.com/AxSaucedo">@AxSaucedo</a><br/>
    Github: <a href="http://github.com/axsauze">AxSauze</a><br/>
  <br />
</p>


[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h2>The Institute for Ethical AI & ML</h2>
<h3>The state of MLOps in 2019</h3>

<table class="bio-table" style="margin-top: -30px">
  <tr>
    <td style="float: left">
        <br>
        ![portrait](images/alejandro.jpg)
        <br>
        <font style="font-weight: bold; color: white">Alejandro Saucedo</font>
        <br>
        Twitter: <a href="">@AxSaucedo</a><br/><br/>
        <br>
    </td>
    <td style="float: left; color: white; font-size: 0.7em;">

        <br>
        Chief Scientist
        <br>
        <a style="color: cyan" href="http://e-x.io">The Institute for Ethical AI & ML</a
        <br>
        <br>
        <br>
        <hr>
        <br>
        Head of Solutions Eng. & Sci.
        <br>
        <a style="color: cyan" href="http://eigentech.com">Eigen Technologies</a>
        <br>
        <br>
        Chief Technology Officer
        <br>
        <a style="color: cyan" href="#">Hack Partners</a>
        <br>
        <br>
        Software Engineer
        <br>
        <a style="color: cyan" href="#">Bloomberg LP.</a>

    </td>
  </tr>
  <tr>
  </tr>
</table>


[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->
### Scalable Machine Learning
https://bit.ly/mlops19

### Awesome MLOps List
http://bit.ly/awesome-mlops


[NEXT]
<!-- .slide: data-background="images/particles.gif" class="background smallquote" -->
## #LetsDoThis

[NEXT SECTION]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
# 1. Motivations


[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
Data science generalised in two workflows

* Model Development
* Model Serving

![classification_large](images/ml-pipeline.png)
<!-- .element: style="background-color: white !important" -->

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->

If we have a small data science project...
* Small number of models to maintain
* Knowledgee in head of data scientists, engineers, etc
* Each has own methods for tracking progress
* The impact of errors is relatively lower

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->


<br>
### It all works relatively well!


[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->

# However
As our data science requirements grow...
## We face new issues

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
#### Increasing complexity in flow of data
<div class="left-col">
    <ul>
        <li>Large number of data processing workflows</li>
        <li>Data is modified without stardardised trace</li>
        <li>Managing complexity of flows and scheduling becomes unmanagable</li>
    </ul>
</div>
<div class="right-col">
![classification_large](images/crontab.jpg)
</div>

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
#### Each data scientist has their own set of tools

<div class="left-col">
    <ul>
        <li>Some ♥ Tensorflow</li>
        <li>Some ♥ R</li>
        <li>Some ♥ Spark</li>
    </ul>
</div>
<div class="right-col">
![classification_large](images/mlibs.jpg)
</div>

<br style="clear:both">
### Some ♥ all of them


[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->

#### Serving models becomes increasinly harder

<div class="left-col">
![classification_large](images/mlmodles.png)
</div>
<div class="right-col">
    <ul>
        <li>Different model versions running in different environments</li>
        <li>Deploying and reverting models gets increasingly complex</li>
    </ul>
</div>

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
#### When stuff goes wrong it's hard to trace back

<div class="left-col">
![classification_large](images/gitblame.jpg)
</div>

<div class="right-col">
    <ul>
        <li>Data scientists say it's a bug in the pipelines</li>
        <li>Data engineers say it's something wrong in the models</li>
        <li>Black box models are develeloped without explainability in mind</li>
    </ul>
</div>

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
## It's challenging
![classification_large](images/mleng-roles.png)


[NEXT SECTION]

# 2. Eco

[NEXT]

### As your technical functions grow...

![classification_large](images/mltemp1.png)

[NEXT]

### So should your infrastructure

![classification_large](images/mlops1.png)

[NEXT]

### The 2 principles of ML-Ops
* Reproducibility
* Orchestration

![classification_large](images/mlops2.png)

[NEXT]

Let's break down the two general principles

[NEXT]

# Principle I
## Model & Data Versioning

![classification_large](images/mltemp6.png)

The age-old question of reproducibility in data science

[NEXT]

### Dissecting each step in our pipelines

![classification_large](images/mltemp2.png)

Each stage has code/config, as well as specific data in/out 

[NEXT]

## Abstracting individual steps

![classification_large](images/mlstep.png)


<div style="float: left; width: 33%">
<h4>Data in </h4>

<pre><code class="code python hljs" style="font-size: 0.6em; line-height: 1em">
$ cat data-input.csv

>            Date    Open    High     Low   Close     Market Cap
> 1608 2013-04-28  135.30  135.98  132.10  134.21  1,500,520,000
> 1607 2013-04-29  134.44  147.49  134.00  144.54  1,491,160,000
> 1606 2013-04-30  144.00  146.93  134.05  139.00  1,597,780,000

</code></pre>
</div>

<div style="float: left; width: 33%">
<h4>Code / Config</h4>
<pre><code class="code python hljs" style="font-size: 0.6em; line-height: 1em">
$ cat feature-extractor.py

> def open_norm_feature_extractor(df):
>     feature = some_lib.get_open(df)
>     return feature


</code></pre>
</div>

<div style="float: left; width: 33%">
<h4>Data out</h4>
<pre><code class="code python hljs" style="font-size: 0.6em; line-height: 1em">
$ cat data-output.csv

>   Open 
>   0.57 
>   0.59 
>   0.47 

</code></pre>
</div>


[NEXT]

<div style="position: absolute; width: 30%; right: 0; bottom: -5%">
![classification_large](images/versioning.jpg)
</div>
## Going one level higher

We can abstract our entire pipeline and data flows

![classification_large](images/mltemp5.png)

_note_
Similarly we can store the accuracy of the model
Together with all the parameters that were used to compute it


[NEXT]

This gets us closer to our ultimate objective:

# Reproducibility

[NEXT]

## Reproducibility enables for
* Traceablility when debugging for errors
* Transparency on the steps that lead to results
* Modularity of components so they can be reused
* Abstraction to support multiple libraries 
* Robustness if we need to go back to a previous release

[NEXT]

Once we have our internal representations for our models...

### We are able to serve them in production

[NEXT]

# Principle II 
### Model Deployment Orchestration

![classification_large](images/mltemp3.png)

Covers complexities of serving models in production

[NEXT]

#### Similar to CI / CD / Monitoring for software...

# But completely different

_note_
And it's different because we are not dealing with 
"just software"...

[NEXT]

### A. Karpathy on Software 2.0 (AKA ML)

1) We specify some goal on the behavior of a desirable program (instead of coding it)
```
(e.g., “satisfy a dataset of input-output pairs of examples,” 
or, “win a game of Go”)
```
2) write a rough skeleton of the code
```
(e.g., a neural net architecture) that identifies a 
subset of program space to search, 
```
3) use the computational resources at our disposal to search this space for a program that works.

[NEXT]

Let's see how this differs

[NEXT]

# Monitoring 

### Going beyond debug logs

[NEXT]

# Monitoring 

<div class="left-col">
<h3>Short term</h3>

<ul>
    <li>Anomalies </li>
    <li>Bias</li>
    <li>Comp. vs prev model</li>
</ul>
</div>

<div class="right-col">
<h3>Long term</h3>
<ul>
    <li>Errors</li>
    <li>Outages</li>
    <li>Performance</li>
</ul>
</div>

<br style="clear:both">
<br style="clear:both">
### Ensuring short and medium term approaches

[NEXT]

#### Quality control processes in production are 
## necessary 
#### and need to be specific to its usecase

[NEXT]

# Compliance 

<ul>
    <li>What happened</li>
    <li>When it happened</li>
    <li>Why it happened</li>
    <li>How it happened</li>
</ul>

<br>
### A boring word with exciting benefints

[NEXT]

#### We Can stop praying to the demo gods

<div style="width: 40%; float: left">
![classification_large](images/programming-gods.jpg)
</div>

<div style="width: 60%; float: left">
<a href="https://www.youtube.com/watch?v=eOzl-LFqYFM" style="font-size: 0.6em">Guidelines for and properties of compliant ML</a>
![classification_large](images/compliant-ml.png)
<a href="https://www.youtube.com/watch?v=eOzl-LFqYFM" style="font-size: 0.6em">CNCF 2018 - Pachyderm</a>
</div>
<br style="clear: both">


[NEXT]

This enables the data scientists, data engineers, and devops/mlops engineers to:
* Trace back issues
* Debug problems
* Report critical issues
</div>


[NEXT]

## Computational Resource allocation

Services with different computational requirements

With often complex computational graphs

We need to be able to allocate the right resources


[NEXT]

## This is a hard problem

It's basically an operating system kernel

where physical resources have to be abstracted

and the "software" can be:
* An ETL framework
* A HDFS-based service 
* A Kubernetes cluster
* Any distibuted framework!



[NEXT]

#### Resource allocation Makes a difference

![classification_large](images/arch3.png)

Compare traditional server allocation

[source: <a href="https://algorithmia.com/">Algorithmia</a>]

[NEXT]

#### Resource allocation Makes a difference

![classification_large](images/arch2.png)

To auto-scale 

[source: <a href="https://algorithmia.com/">Algorithmia</a>]

[NEXT]

#### Resource allocation Makes a difference

![classification_large](images/arch1.png)

Even to serverless

[source: <a href="https://algorithmia.com/">Algorithmia</a>]


[NEXT]

So now we understand some of the implications

## What's next?

### Let's have a look at some solutions

[NEXT SECTION]

# 3. Existing Tools

[NEXT]

I'm putting together a list in Github on

# "Awesome MLOps"

with the tools available for ML Operations

## Feel free to chip in!

<br>
#### <a href="bit.ly/awesome-mlops">bit.ly/awesome-mlops</a>


[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h1><font style="color:#76f0ff">ML</font>Ops / <font style="color:#76f0ff">Data</font>Ops</h1>
<h4>a curated list of frameworks to scale<br> your <font style="color:#76f0ff">machine learning</font> capabilities<br></h4>
<p>
  <br />
  <a style="color:#76f0ff" href="">bit.ly/awesome-mlops</a>
  <br />
  <br />
</p>
<p>


[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h1>The <font style="color:#76f0ff">AI</font>/<font style="color:#76f0ff">ML</font> Principles</font></h1>
<h4>A practical <font style="color:#76f0ff">industry framework</font> to develop<br> <font style="color:#76f0ff">AI</font> & <font style="color:#76f0ff">machine learning</font> systems <font style="color:#76f0ff">responsibly</font></h4>
  <br />
  <h4><a style="color:#76f0ff" href="">http://ethical.institute/</a></h4>
  <br />
  <br />
<p>



[NEXT]

# Principle I 
## Reproducibility
Model and data versioning

[NEXT]

## PMML

A standard way of representing machine learning model pipelines for storage and serialisation

<iframe src="http://dmg.org/pmml/v4-1/GeneralStructure.html" frameborder="0" style="width: 100%; height: 40vh"></iframe>

Several systems use it to transfer models across platforms

[NEXT]
## PMML

#### Exporting to PMML using sklearn2pmml
```
from sklearn import datasets, tree
iris = datasets.load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

from sklearn_pandas import DataFrameMapper
default_mapper = DataFrameMapper(
    [(i, None) for i in iris.feature_names + ['Species']])

from sklearn2pmml import sklearn2pmml
sklearn2pmml(estimator=clf,
             mapper=default_mapper,
             pmml="D:/workspace/IrisClassificationTree.pmml")
```

[NEXT]

## Data Version Control (DVC)

A full-on Open-source Version Control System for Data Science Projects

<div class="left-col">
<br>
A fork of git, built by iterative.ai, that allows for grouping data, 
config and code through a version control system
</div>

<div class="right-col">
![classification_large](images/dvc.png)
</div>



[NEXT]

## Data Version Control (DVC)

#### Add your data

```
dvc add images.zip
```

#### Connect data input, model output and code

```
dvc run -d images.zip -o model.p ./cnn.py
```

#### Add repository location (here is s3)

```
dvc remote add myrepo s3://mybucket
```

#### Push to the location specified

```
dvc push
```

[NEXT]

## ModelDB

A more implicit way of tracking the inputs, outputs and configurations on a library-level by extending the functions themselves. 

<div class="left-col">
<h4>Normal sklearn</h4>

<pre><code class="code python hljs" style="font-size: 1em; line-height: 1em">
def fit_and_predict(data):
    model.fit(data)
    preprocessor.transform(data)
    model.predict(data)

</code></pre>
</div>


<div class="right-col">
<h4>ModelDB-enabled</h4>

<pre><code class="code python hljs" style="font-size: 1em; line-height: 1em">
def fit_and_predict(data):
    model.fit_sync(data)
    preprocessor.transform_sync(data)
    model.predict_sync(data)

</code></pre>
</div>

This basically stores all the steps that were used, together with the results and predictions of the model


[NEXT]

## ModelDB

This allows for exploration of models that have been run

<!--<iframe src="http://modeldb.csail.mit.edu:3000/projects/1/models" frameborder="0" style="width: 100%; height: 50vh"></iframe>-->
<iframe src="https://mitdbg.github.io/modeldb/" frameborder="0" style="width: 100%; height: 50vh"></iframe>

[NEXT]

# Pachyderm 

![classification_large](images/pachyderm.png)

Pachyderm is an end-to-end model-versioning framework that allows for reproducible pipeline definitions.

[NEXT]

## Pachyderm

Pachyderm consists of three main components:
* Data "repositories"
* Processing steps wrapped in docker containers
* Pipelines that connect steps and data repositories

<br>
#### Each step contains an input and output of data

[NEXT]

## Pachyderm Example

Building a training pipeline for iris classifier

Using sklearn svm, output a training model


[NEXT]

## Create a repo and add data

Create a repo
```
$ pachctl create-repo training
$ pachctl list-repo
NAME                CREATED             SIZE
training            2 minutes ago       0 B
```

Commit data (with -c flag) into the repository
```
$ pachctl put-file training master -c -f data/iris.csv
```

[NEXT]

## Build your docker image


<div class="left-col">
<h4>pytrain.py</h4>

<pre><code class="code python hljs" style="font-size: 0.6em; line-height: 1em"># pytrain.py

...import dependencies
 
cols = [ "Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width", "Species" ]
features = [ "Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width" ]

# Load training data
irisDF = pd.read_csv(os.path.join("/pfs/training", 
    "iris.csv"), names=cols)

svc = svm.SVC(kernel='linear', C=1.0).fit(
    irisDF[features], irisDF["Species"])

# Save model to pachyderm /pfs/out
joblib.dump(svc, os.path.join("/pfs/out", 'model.pkl'))

</code></pre>
</div>


<div class="right-col">
<h4>Dockerfile</h4>

<pre><code class="code python hljs" style="font-size: 1em; line-height: 1em">
FROM ubuntu:14.04

...install dependencies 

# Add our own code.
WORKDIR /code
ADD pytrain.py /code/pytrain.py


</code></pre>
</div>

[NEXT]

## Define computational pipeline

```
{
  "pipeline": {
    "name": "model"
  },
  "transform": {
    "image": "pachyderm/iris-train:python-svm",
    "cmd": ["python3", "/code/pytrain.py",]
  },
  "input": {
    "atom": {
      "repo": "training",
      "glob": "/"
    }
  }
}
```

[NEXT]

## Reproducible pipeline

![classification_large](images/iris.png)

# Now what?


[NEXT]

# Principle II
## Orchestration
Model Deployment Orchestration

[NEXT]

## MLeap

Diving one level deeper into serialization of models

<div class="left-col">
![classification_large](images/mleapruntime.jpg)
</div>
<div class="right-col">
<br>
MLeap is used in open source projects that look to abstract the serialisation, execution of various machine learning libraries.
</div>

[NEXT]

## MLeap Serving
Run the server
```
$ docker run \ 
    -p 65327:65327 \
    -v /tmp/models:/models \
    combustml/mleap-serving:0.9.0
```
Load a model
```
curl -XPUT -H "content-type: application/json" \
  -d '{"path":"/models/<my model>.zip"}' \
  http://localhost:65327/model
```

[NEXT]

## MLeap Optimized bundles

![classification_large](images/mleapbundle.png)


[NEXT]

## Seldon-core

![classification_large](images/seldon1.png)

"Machine Learning Deployment for Enterprise"

[NEXT]

![classification_large](images/seldon3.png)
## Strong focus on model orchestration
![classification_large](images/seldon2.png)

[NEXT]

### Tackling the CI/CD challenge
![classification_large](images/cicd.png)

[NEXT]

### Enabling monitoring with grafana
![classification_large](images/dashboard.png)

[NEXT]

# What about us?
### We built our infrastructure:
* Nightly accuracy monitoring framework
* Internal JSON standard for metadata model versioning
* Distributed manager-worker rabbitmq architecture
* Generalised abstraction layer above ML libraries
* SDK interface to extend pipelines 
* End to end data pipeline framework
* Internal machine learning data labelling tools

[NEXT]

# What about you?

[NEXT SECTION]
<!-- .slide: data-background="images/network-background.jpg" class="background smallest" -->

## Scalable Machine Learning
> Motivations
> <br>
> <br>
> Concepts
> <br>
> <br>
> Existing Tools

####  Slides at: <a style="color: cyan" href="#">bit.ly/awesome-mlops</a>


[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->
### Scalable Machine Learning
https://bit.ly/scalable-data-science

### Awesome MLOps List
http://bit.ly/awesome-mlops

[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h2>Scalable Machine Learning</h2>
<h4>The state of DataOps / MLOps in 2018</h4>

<table class="bio-table">
  <tr>
    <td style="float: left">
        ![portrait](images/alejandro.jpg)
        <br>
        <font style="font-weight: bold; color: white">Alejandro Saucedo</font>
        <br>
        <br>
    </td>
    <td style="float: left; color: white; font-size: 0.7em;">

        Head of Solutions Eng./Science
        <br>
        <a style="color: cyan" href="http://e-x.io">Eigen Technologies</a
        <br>
        <br>
        <br>
        Chairman
        <br>
        <a style="color: cyan" href="http://ethical.institute">The Institute for Ethical AI & ML</a>
        <br>
        <br>
        Member, Broader AI Expert Group
        <br>
        <a style="color: cyan" href="#">European Commission</a>
        <br>
        <br>
        Advisory group
        <br>
        <a style="color: cyan" href="http://teensinai.com">TeensInAI</a>
        <br>

    </td>
  </tr>
  <tr>
  </tr>
</table>
  



