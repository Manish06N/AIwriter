from .gpt_providers.openai_chat_completion import openai_chatgpt
import google.generativeai as genai


def generate_blog_title(blog_meta_desc, gpt_providers):
    """
    Given a blog title generate an outline for it
    """
    prompt = f"""As a SEO expert and content writer, I will provide you with meta description of blog. 
        Your task is write a SEO optimized, call to action and engaging blog title for it.
        Follows SEO best practises to suggest the blog title. 
        Please keep the titles concise, not exceeding 60 words, and ensure to maintain their meaning. 
        Respond with only one title and no description or keyword like Title: 
        Generate blog title for this given meta description: {blog_meta_desc}
        """
   if 'gemini' in gpt_providers:
        try:
            genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        except Exception as err:
            logger.error("Failed in getting GEMINI_API_KEY")
        # Use gemini-pro model for text and image.
        model = genai.GenerativeModel('gemini-pro')
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as err:
            logger.error("Failed to get response from gemini.")
    elif 'openai' in gpt_providers:
        try:
            response = openai_chatgpt(prompt)
            return response
        except Exception as err:
            SystemError(f"Error in generating blog summary: {err}") 
