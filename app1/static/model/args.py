import argparse


def parse_args():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument('--model_name_or_path', type=str, default='unified_transformer-12L-cn-luge',
                        help='the transformer pretrain model')
    parser.add_argument('--min_dec_len', type=int, default=0, help='the minimum sequence length of generation')
    parser.add_argument('--max_dec_len', type=int, default=64, help='the maximum sequence length of generation')
    parser.add_argument('--num_return_sequence', type=int, default=20,
                        help='the number of returned sequence for one input in generation')
    parser.add_argument('--decode_strategy', type=str, default='sampling',
                        help='the decode strategy in generation')
    parser.add_argument('--top_k', type=int, default=5,
                        help='the number of highest probability vocabulary tokens to keep for top-k sampling')
    parser.add_argument('--device', type=str, default='gpu', help='the device to select for training the model')

    args = parser.parse_args(args=[])
    return args