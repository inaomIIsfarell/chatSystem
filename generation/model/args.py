import argparse


def parse_args():
    parser = argparse.ArgumentParser(__doc__)

    parser.add_argument('--model_name_or_path', type=str, default='unified_transformer-12L-cn-luge')
    parser.add_argument('--min_dec_len', type=int, default=0)
    parser.add_argument('--max_dec_len', type=int, default=64)
    parser.add_argument('--num_return_sequence', type=int, default=20)
    parser.add_argument('--decode_strategy', type=str, default='sampling')
    parser.add_argument('--top_k', type=int, default=5)
    parser.add_argument('--device', type=str, default='gpu')

    args = parser.parse_args(args=[])
    return args
