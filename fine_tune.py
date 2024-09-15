import psycopg2
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


conn = psycopg2.connect(
    dbname="doc_retrieval", user="ananya", password="mde6133#K", host="localhost", port = "5432"
)
cur = conn.cursor()

# Fetch documents from PostgreSQL
cur.execute("SELECT content FROM documents")
rows = cur.fetchall()

train_examples = []
for i in range(len(rows) - 1):
    content1 = rows[i][0]
    content2 = rows[i + 1][0]
    similarity_score = 0.5  # Assign similarity scores based on your domain knowledge
    train_examples.append(InputExample(texts=[content1, content2], label=similarity_score))


train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)


train_loss = losses.CosineSimilarityLoss(model=model)


model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=4, warmup_steps=100)


output_dir = './fine_tuned_model_postgresql'
model.save(output_dir)


cur.close()
conn.close()