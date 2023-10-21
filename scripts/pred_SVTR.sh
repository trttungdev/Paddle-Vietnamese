python tools/infer/predict_rec.py --image_dir="../BKAI2023/new_public_test" \
                                    --use_gpu=True \
                                    --rec_algorithm="SVTR" \
                                    --rec_model_dir="../weight_models/SVTR/Inference/"  \
                                    --rec_image_shape="3, 32, 128"  \
                                    --rec_char_dict_path="vi_vietnam.txt" \
                                    > prediction_log.txt
