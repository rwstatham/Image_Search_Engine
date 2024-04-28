# Image_Search_Engine
<ul>
<h2>
  <li> An animal image search engine that returns the images in the database that are most similar to the queried image. Implemented through a vector database service, <u> Weaviate </u>. </li>
  <li> Weaviate database hosted in a <u>Docker</u> container that can be run locally. </li>
  <li> Search engine implemented through Python and <u>Weaviate</u>.</li>
</h2>
</ul>

<h3> Docker Container Setup </h3>
The implementation described below <b>assumes you have the Docker Desktop app installed</b>. <br>
Use the following command in the command prompt to initialize the containers: <br>
<pre> curl -o docker-compose.yml "https://configuration.weaviate.io/v2/docker-compose/docker-compose.yml?generative_anyscale=false&generative_aws=false&generative_cohere=false&generative_mistral=false&generative_openai=false&generative_palm=false&image_neural_model=pytorch-resnet50&media_type=image&modules=modules&ref2vec_centroid=false&reranker_cohere=false&reranker_transformers=false&runtime=docker-compose&weaviate_version=v1.24.10&weaviate_volume=no-volume" </pre>
Next, simply issue the following command to activate your containers:
<pre> docker-compose up -d </pre>

<h3>Programs Overview:</h3> 
Below, we discuss all programs present in the repository and discuss their uses. <br>
<ol type ="I">
  <li> <var>Init_weaviate_client.py</var></li>
    <ul>
      <li> Running this file serves as a test to see if you can connect to the weaviate database successfully.</li>
    </ul>
  <li> <var>def_schema.py</var></li>
    <ul>
      <li> This file contains function definitions that initialize the schema of the database and define the query process respectively.</li>
    </ul>
  <li><var>upload_images.py</var></li>
    <ul>
      <li>This file defines two functions that (1) Clears the database, and (2) converts non-evaluation images into base64 and inserts them into the database.</li>
    </ul>
  <li><var>Full_init.py</var></li>
    <ul>
      <li>This file, when ran, fully initialized the database in one file execution.</li>
    </ul>
  <li><var>query_image.py</var></li>
    <ul>
      <li>This file is where we call the query image function. The user edits the parameters of the query function from this file and run this file to recieve results.</li>
      <li>When running a query, the resulting image(s) will be saved in a <var> Results </var> folder. This folder will be cleared when querying further images. </li>
    </ul>
</ol>

<h3>Data</h3>
<ul>
  <li>DB_images</li>
  <ul>
    <li>Folder of images that are to be inserted into the database.</li>
  </ul>
  <li>Eval_images</li>
  <ul>
    <li>Folder of images held out for querying.</li>
  </ul>
</ul>



