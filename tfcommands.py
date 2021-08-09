python -m scripts.label_image  --graph=tf_files/retrained_graph.pb   --image="C:\School\Extracurricular\Science Fair\2019-2020\VALIDATION_SET_unexposed\Im0016_ORIGA.jpg"

tensorboard --logdir tf_files/training_summaries &

python -m scripts.retrain \  --bottleneck_dir=tf_files/bottlenecks \  --model_dir=tf_files/models/"mobilenet_0.50_224" \  --summaries_dir=tf_files/training_summaries/"mobilenet_0.50_224" \  --output_graph=tf_files/retrained_graph.pb \  --output_labels=tf_files/retrained_labels.txt \  --architecture="mobilenet_0.50_224" \  --image_dir=tf_files/image_data

python -m scripts.retrain \  --bottleneck_dir=tf_files/bottlenecks \  --how_many_training_steps=250 \  --model_dir=tf_files/models/ \  --summaries_dir=tf_files/training_summaries/"mobilenet_0.50_224" \  --output_graph=tf_files/retrained_graph.pb \  --output_labels=tf_files/retrained_labels.txt \  --architecture="mobilenet_0.50_224" \  --image_dir=tf_files/image_data \ --learning_rate=3