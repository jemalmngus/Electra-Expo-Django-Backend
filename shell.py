from main.models import FAQ

faq_data = [
    {
        'question': 'What are the expo dates?',
        'answer': 'The expo will be held from September 9-12, 2023.'
    },
    {
        'question': 'Are there any age restrictions to attend the expo?',
        'answer': 'The expo is open to all age groups. Children under 12 can enter for free.'
    },
    {
        'question': 'Are there any discounted tickets available?',
        'answer': 'Yes, we offer discounted tickets for students upon presenting a valid student ID.'
    },
    {
        'question': 'Is parking available at the venue?',
        'answer': 'Yes, there is ample parking available for attendees at the venue.'
    },
    {
        'question': 'Are there any restrictions on photography or videography?',
        'answer': 'Photography and videography are allowed, but professional equipment and commercial use require prior authorization.'
    },
    {
        'question': 'Can I bring outside food and drinks?',
        'answer': 'Outside food and drinks are not allowed inside the expo hall. However, there will be food stalls and refreshment options available.'
    },
    {
        'question': 'What are the payment methods accepted for tickets?',
        'answer': 'We accept cash, credit cards, and mobile payments for ticket purchases.'
    },
    {
        'question': 'What are the registration fees?',
        'answer': 'Registration fees vary based on the type of registration and package chosen. Please refer to the registration page for detailed information.'
    },
    {
        'question': 'How can I become an exhibitor?',
        'answer': 'To become an exhibitor, please visit the exhibitor registration page and fill out the required information.'
    },
    {
        'question': 'What are the exhibition hall opening hours?',
        'answer': 'The exhibition hall is open from 9:00 AM to 6:00 PM during the expo days.'
    },
    {
        'question': 'Can I make changes to my registration information?',
        'answer': 'Yes, you can make changes to your registration information by contacting our support team or visiting the registration portal.'
    },
    {
        'question': 'Is there a dress code for the expo?',
        'answer': 'There is no strict dress code for the expo. However, we recommend wearing business casual attire.'
    },
    {
        'question': 'Can I get a refund for my registration?',
        'answer': 'Refunds are available based on our refund policy. Please refer to the registration terms and conditions for more information.'
    },
    {
        'question': 'Are there any accommodation options near the venue?',
        'answer': 'Yes, there are several hotels and accommodations available in close proximity to the venue. You can find a list of recommended accommodations on our website.'
    },
    {
        'question': 'Are there any networking events during the expo?',
        'answer': 'Yes, we organize various networking events, seminars, and workshops for attendees to network and engage with industry professionals.'
    },
    {
        'question': 'Can I bring my pet to the expo?',
        'answer': 'Pets are not allowed inside the expo hall, except for service animals.'
    },
]


for entry in faq_data:
    faq = FAQ(question=entry['question'], answer=entry['answer'])
    faq.save()

all_faqs = FAQ.objects.all()
for faq in all_faqs:
    print(f"Question: {faq.question}")
    print(f"Answer: {faq.answer}")
    print("----------")

# exec(open('shell.py').read())
