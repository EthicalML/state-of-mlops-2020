
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h2>The Institute for Ethical AI & ML</h2>
<h3>The state of Production ML in 2020</h3>
<p>
  <br />
  <br />
    Alejandro Saucedo | <a href="">a@ethical.institute</a><br/><br/>
    Twitter: <a href="http://twitter.com/AxSaucedo">@AxSaucedo</a><br/>
  <br />
</p>

[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h2>The Institute for Ethical AI & ML</h2>

<h4>The state of Production ML in 2020</h4>

<table class="bio-table">
  <tr>
    <td style="float: left">
        <br>
        ![portrait](images/aletechuk.png)
        <br>
        <font style="font-weight: bold; color: white">Alejandro Saucedo</font>
        <br>
        Twitter: <a href="https://twitter.com/axsaucedo">@AxSaucedo</a>
    </td>
    <td style="float: left; color: white; font-size: 0.7em;">

        <br>
        Chief Scientist
        <br>
        <a style="color: cyan" href="http://e-x.io">The Institute for Ethical AI & ML</a
        <br>
        <br>
        <br>
        Engineering Director
        <br>
        <a style="color: cyan" href="#">Seldon Technologies</a>
        <br>
        <br>
        <hr>
        <br>
        Head of Solutions Eng. & Sci.
        <br>
        <a style="color: cyan" href="http://eigentech.com">Eigen Technologies</a>
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
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

![classification_large](images/seldon3.png)

## OSS ML Serving in k8s
![classification_large](images/seldon2.png)

#### We're hiring: <a href="https://seldon.io">seldon.io</a>

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## The Institute for Ethical AI & Machine Learning

![classification_large](images/institute.png)

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## We are part of the Linux Foundation AI 

![classification_large](images/lfai-institute.jpg)


[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->

## Small data science projects
![classification_large](images/ml-pipeline.png)
<!-- .element: style="background-color: white !important" -->

### Works relatively well


[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->

# However
As our data science requirements grow...
## We face new issues

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
#### Increasing complexity in flow of data
![classification_large](images/crontab.jpg)

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
![classification_large](images/mlmodles.png)

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
#### When stuff goes wrong it's hard to trace back
![classification_large](images/gitblame.jpg)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

### As your technical functions grow...

![classification_large](images/mltemp1.png)

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

### So should your infrastructure

![classification_large](images/mlops1.png)

[NEXT]
<!-- .slide: data-background="images/parti.png" class="background smallquote" style="color: white" -->
## It's challenging
![full_height](images/mleng-roles.png)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Mapping the Ecosystem 

![](images/lfai-landscape.jpg)

### https://landscape.lfai.foundation



[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Principles today
<br>

<div class="left-col" style="width: 40%; padding-top: 25px">
<ul>
    <li>Orchestration</li>
    <li>Explainability</li>
    <li>Reproducibility</li>
</ul>
</div>

<div class="right-col" style="width: 60%">
<img src="images/mlops2.png" alt="">
</div>

[NEXT SECTION]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

# 2.1 Model Orchestration

![classification_large](images/mltemp3.png)

### Training & serving at scale


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Computational Resource allocation

Services with different computational requirements

With often complex computational graphs

We need to be able to allocate the right resources

<br>
### This is a hard problem


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Adding Governance/Compliance

![classification_large](images/mleng-expertise.png)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Standardisation of metrics

![classification_large](images/grafana.jpg)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Standardisation of errors

![classification_large](images/kibana.jpg)

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Complex Deployment Strategies

![classification_large](images/inferencepipe.png)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Hands on example using:

![](https://raw.githubusercontent.com/SeldonIO/seldon-core/master/doc/source/seldon.png)

#### Seldon core is an OSS library for  machine learning orchestration and monitoring in production

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Basic Example:

Wrapping an [income classifier Python model](https://github.com/SeldonIO/seldon-core/tree/master/examples/explainers/alibi_anchor_tabular)

![classification_large](images/simple-model.jpg)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## GitOps Strategies for ML

![classification_large](https://raw.githubusercontent.com/axsaucedo/seldon-core/pytorch_hub/examples/models/pytorchhub/images/pytorchhub-seldondep-overview.jpg)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## More advanced Example:

PyTorch Hub Deployment: https://bit.ly/pytorchseldon

![classification_large](images/pytorchhub.jpg)





[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Other libraries to watch

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## KFServing

Serverness for machine learning in kubernetes based on Knative

![classification_large](https://raw.githubusercontent.com/kubeflow/kfserving/master/docs/diagrams/kfserving.png)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->
## DeepDetect

Unifying multiple external machine learning libraries on a single API

![classification_large](images/deepdetect.png)

#### <a href="https://www.deepdetect.com/">www.deepdetect.com/</a>


[NEXT SECTION]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->
# 2.2 Explainability
Tackling "black box model" situations

![classification_large](images/mlops2.png)

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->
## Going beyond the algorithms 
Explainability through tools, process and domain expertise.
![classification_large](images/bias.png)

[Our talk on <a href="https://www.youtube.com/watch?v=GZpfBhQJ0H4">Explainability of Tensorflow Models</a>]


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Data assessment

<div class="left-col">
<br>
<ul>
    <li>Class imbalances</li>
    <li>Protected features</li>
    <li>Correlations</li>
    <li>Data representability</li>
</ul>
</div>
<div class="right-col">
<img src="images/class-imbalance.png" alt="">
</div>

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Model assessment

<div class="left-col">
<img src="images/shap-values.png" style="background-color: white !important" alt="">
</div>
<div class="right-col">
<br>
<ul>
    <li>Feature importance</li>
    <li>Model specific methods</li>
    <li>Domain knowledge abstraction</li>
    <li>Model metrics analysis</li>
</ul>
</div>


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Production monitoring


<div class="left-col">
<img src="images/roc-monitoring.png" alt="">
</div>
<div class="right-col">
<ul>
    <li>Evaluation of metrics</li>
    <li>Manual human review</li>
    <li>Monitoring of anomalies</li>
    <li>Setting thresholds for divergence</li>
</ul>
</div>

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Infrastructure level XAI Design patterns 

![classification_large](https://ethicalml.github.io/explainability-and-bias/images/prodxai-5a.jpg)

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Hands on example using:

<img style="height: 30vh;background-color: white !important" src=https://raw.githubusercontent.com/SeldonIO/alibi/master/doc/source/_static/Alibi_Logo.png>

#### Alibi is a library that contains production-level black box model explainability techniques




[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Example

Deploying Explainer Modules: http://bit.ly/seldonexplainer

![classification_large](images/alibi.jpg)



[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Other OSS libraries to watch


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## ELI5
![classification_large](images/eli5-text.png)

#### <a href="https://github.com/TeamHG-Memex/eli5">github.com/TeamHG-Memex/eli5</a>


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->
## SHAP

Unifying multiple model explainability techniques

![classification_large](images/minst-image-plot.png)
<!-- .element: style="background-color: white !important" -->

#### <a href="https://github.com/slundberg/shap">github.com/slundberg/shap</a>

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->
## XAI
Analyse datasets, evaluate models and monitor production

![classification_large](images/xai-pr.png)

#### <a href="https://github.com/ethicalml/xai">github.com/ethicalml/xai</a>


[NEXT SECTION]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->
# 2.3 Reproducibility
![classification_large](images/mltemp6.png)
### Model & data versioning


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

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
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

<div style="position: absolute; width: 30%; right: 0; bottom: -5%">
![classification_large](images/versioning.jpg)
</div>
## Going one level higher

We can abstract our entire pipeline and data flows

![classification_large](images/mltemp5.png)

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Hands on example using:

<img style="height: 30vh" src="https://camo.githubusercontent.com/bd4adfc06b0e349c47f2bae3319544a2e547c796/68747470733a2f2f7777772e6b756265666c6f772e6f72672f696d616765732f6c6f676f2e737667">

#### Kubeflow is a Cloud Native platform for reusable machine learning pipelines in kubernetes 


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Example

Reusable NLP Pipelines: https://bit.ly/seldon-kf-nlp

![classification_large](images/kubeflowexample.jpg)


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Other OSS libraries to watch

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Data Version Control (DVC)


#### Add your data

```
dvc add images.zip
```

#### commit data input, model output and code

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

#### Check it out at <a href="https://dvc.org">dvc.org</a>

[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## MLFlow

![classification_large](images/mlflow.png)

#### http://github.com/databricks/mlflow


[NEXT]
<!-- .slide: data-background="images/partistat.png" class="background smallquote" style="color: white" -->

## Pachyderm 
![classification_large](images/pachyderm-dashboard.png)

#### <a href="https://www.pachyderm.io/">www.pachyderm.io/</a>
[NEXT SECTION]
<!-- .slide: data-background="images/network-background.jpg" class="background smallest" -->

## Much more content


||||
|-|-|-|
|[🔍 Explainability](https://github.com/EthicalML/awesome-machine-learning-operations#1-explaining-black-box-models-and-datasets) |[🔏 Privacy](https://github.com/EthicalML/awesome-machine-learning-operations#2-privacy-preserving-machine-learning) | [📜 Versioning](https://github.com/EthicalML/awesome-machine-learning-operations#3-model-and-data-versioning)|
|[🏁 Orchestration](https://github.com/EthicalML/awesome-machine-learning-operations#4-model-deployment-and-orchestration-frameworks)|[🌀 FeaturEng](https://github.com/EthicalML/awesome-machine-learning-operations#5-feature-engineering-automation)|[🤖 AutoML](https://github.com/EthicalML/awesome-machine-learning-operations#6-neural-architecture-search)|
| [📓 Notebooks](https://github.com/EthicalML/awesome-machine-learning-operations#7-data-science-notebook-frameworks) | [📊 Visualisation](https://github.com/EthicalML/awesome-machine-learning-operations#8-industrial-strength-visualisation-libraries) | [🔠 NLP](https://github.com/EthicalML/awesome-machine-learning-operations#9-industrial-strength-nlp) |
| [🧵 ETL](https://github.com/EthicalML/awesome-machine-learning-operations#10-data-pipeline-etl-frameworks) | [🗞️ Storage](https://github.com/EthicalML/awesome-machine-learning-operations#11-data-storage-optimisation) | [📡 FaaS](https://github.com/EthicalML/awesome-machine-learning-operations#12-function-as-a-service-frameworks) |
| [🗺️ Computation](https://github.com/EthicalML/awesome-machine-learning-operations#13-computation-load-distribution-frameworks) | [📥 Serialisation](https://github.com/EthicalML/awesome-machine-learning-operations#14-model-serialisation-formats) | [🎁 Compiler](https://github.com/EthicalML/awesome-machine-learning-operations#15-compiler-optimisation-frameworks)  |
| [💸 CommercialML](https://github.com/EthicalML/awesome-machine-learning-operations#16-commercial-data-science-platforms) | [💰 CommercialETL](https://github.com/EthicalML/awesome-machine-learning-operations#17-commercial-etl-platforms)| |
<br>
### Check it out & add more libraries

[NEXT]
<!-- .slide: data-background="images/network-background.jpg" class="background" -->

<h2>The Institute for Ethical AI & ML</h2>

<h4>The state of Production ML in 2020</h4>

<table class="bio-table">
  <tr>
    <td style="float: left">
        <br>
        ![portrait](images/aletechuk.png)
        <br>
        <font style="font-weight: bold; color: white">Alejandro Saucedo</font>
        <br>
        Twitter: <a href="https://twitter.com/axsaucedo">@AxSaucedo</a>
    </td>
    <td style="float: left; color: white; font-size: 0.7em;">

        <br>
        Chief Scientist
        <br>
        <a style="color: cyan" href="http://e-x.io">The Institute for Ethical AI & ML</a
        <br>
        <br>
        <br>
        Engineering Director
        <br>
        <a style="color: cyan" href="#">Seldon Technologies</a>
        <br>
        <br>
        <hr>
        <br>
        Head of Solutions Eng. & Sci.
        <br>
        <a style="color: cyan" href="http://eigentech.com">Eigen Technologies</a>
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



