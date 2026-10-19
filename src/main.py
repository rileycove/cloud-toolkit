from src.pipeline import process_batch

def run():
    sample_data = [{'id': 1, 'active': True}, {'id': 2, 'active': False}]
    result = process_batch(sample_data)
    print(f"[cloud-toolkit] Batch finished: {result}")

if __name__ == '__main__':
    run()