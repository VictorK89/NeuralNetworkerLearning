# Victor K.
# NeuralNetworkerLearning

result_regressor_nomen is the result with the added 0/1 vectors to the word vectors
result_regressor_basic_old ist the old result without anything

How it worked:

Get the Wordlist / "Nomen" list / whatever list you want with "own_test1.py" via either the whole "train.conll" or parts of it ("train_data1-10.conll"); it was split it 10 even parts.

Since we got the "german_model_wordlist.txt" we can now get the right index of each line (word) from our "wordlist_annotations1-10" to "annotations_index_from_embeddings_1-10", we mark the words we lack with a "-1".

If we delete all lines that are not "-1" we get all usable word indexes ("annotations_index_from_embeddings_not_one_1-10")

That are now our vector indexes, we can grab the "vector_list_usable_1-10" with "index_test4.py" from our big overall vector list.

Similiar we can get another index list for what is needed for the wordlist_annotations_1-10 to wordlist_annotations_usable_1-10 (or in fact every other list, like top_or_not_usable_1-10 from top_or_not_list_annotations_1-10) with the indexes "index_minus_one_annotations_from_embeddings_1-10" again with "index_test4.py".

Similiar we got the "nomen_annotations_1-10" list and the following "nomen_list_usable_1-10"

We replaced the content to 52 zeros and one 1 (sadly we had to cheat and "pre_replace" first, cause PTKNEG and APPRART contain other words we want to replace, we do this with "pre_replace_nomen.py", we then can replace the "pre_replaced" lists with "replace_nomen.py", here the jobs get done.)

We zip the vector lists and nomen lists together to "vector_nomen_1-10" with "zip.py"

We alrdy had replaced the top_or_not lists to 1/0 and made also a tupel list.

We can now run the "test_theanet1.py" with either the vector_nomen or the basic vector lists as input and top_or_not list as output, we save the model and iterate 1-9 times and then predict with the 10th time.

We measure our precision with "thresholds.py" (and don't know what is happening when our vector_nomen lists achieve a worse result then our basic vector lists)
