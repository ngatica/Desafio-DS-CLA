import re
import nltk

def preprocess_word(word):
    """
    Función que preprocesa una palabra, eliminando puntuaciones y caracteres que no son relevantes para el análisis.
    Toma una palabra como entrada y devuelve la palabra procesada.
    """
    # Eliminar puntuaciones
    word = word.strip('\'"?!,.():;')
    # Convertir más de 2 repeticiones de letras a 2 letras
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Eliminar - y '
    word = re.sub(r'(-|\')', '', word)
    return word

def is_valid_word(word):
    """
    Función que determina si una palabra es válida para ser utilizada en el análisis de sentimientos.
    Devuelve True si la palabra comienza con una letra del alfabeto y no contiene caracteres especiales, números ni puntos.
    """
    # Verificar si la palabra comienza con una letra del alfabeto
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)

def handle_emojis(tweet):
    """
    Función que preprocesa los emojis en un tweet, reemplazándolos por una etiqueta que indique si el emoji es positivo o negativo.
    Devuelve el tweet procesado.
    """
    # Sonreír -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' EMO_POS ', tweet)
    # Risa -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' EMO_POS ', tweet)
    # Amor -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' EMO_POS ', tweet)
    # Guiño -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' EMO_POS ', tweet)
    # Tristeza -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' EMO_NEG ', tweet)
    # Llanto -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', tweet)
    return tweet
