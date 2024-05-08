import json
from crewAI.summarization import ArticleSummarizationCrew
articles = [
    '''
        Artificial Intelligence (AI) has become an integral part of our daily lives, 
        impacting various aspects such as healthcare, finance, and transportation. 
        From virtual assistants like Siri and Alexa to recommendation systems on 
        platforms like Netflix and Amazon, AI algorithms are constantly working in the background 
        to improve user experience. In healthcare, AI is used for diagnosis, treatment planning, 
        and drug discovery, while in finance, it helps in fraud detection and risk management. 
        In transportation, AI powers self-driving cars and optimizes traffic flow. 
        As AI technology continues to advance, its impact on daily life is only expected to grow.
    ''',
    '''
        Artificial Intelligence (AI) is revolutionizing scientific research by enabling scientists to analyze large datasets, 
        simulate complex systems, and discover new patterns and relationships in data. 
        AI algorithms are being used in various scientific fields, including astronomy, 
        biology, chemistry, and physics, to accelerate the pace of discovery. In astronomy, 
        AI is used to analyze astronomical images and identify celestial objects. In biology, 
        AI helps in genomics, drug discovery, and personalized medicine. In chemistry, 
        AI is used for molecular design and materials discovery. In physics, 
        AI is used to analyze particle collision data and simulate complex physical systems
    ''',
    '''
        The gig economy refers to a labor market characterized by short-term and freelance work arrangements, 
        as opposed to traditional full-time employment. In the gig economy, workers, 
        often referred to as "gig workers" or "independent contractors," 
        are hired on a temporary or per-project basis. Popular gig economy platforms include Uber, 
        Lyft, Airbnb, and TaskRabbit. The gig economy offers flexibility and autonomy to workers but also lacks job security 
        and benefits typically associated with traditional employment. Despite these challenges, 
        the gig economy continues to grow, driven by technological advancements and changing attitudes towards work.
    '''
    ]

def summarize_articles(articles):
    crew = ArticleSummarizationCrew()
    summarization_crew = crew.article_summirization_crew()
    results = []
    for article in articles:
        result = summarization_crew.kickoff(inputs = {"article": article})
        results.append(json.loads(result.replace("\\"," ")))
        
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)



if __name__ == "__main__":
    summarize_articles(articles)