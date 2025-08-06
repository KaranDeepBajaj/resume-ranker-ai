from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(jd_text, resume_texts):
    documents = [jd_text] + resume_texts
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    jd_vector = tfidf_matrix[0]
    resume_vectors = tfidf_matrix[1:]

    scores = cosine_similarity(jd_vector, resume_vectors).flatten()
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

    return ranked
