from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
text2 = '''# Python Programming

Python is a popular programming language known for its simple syntax and readability. It is widely used in web development, automation, data analysis, and artificial intelligence.

## Object-Oriented Programming

Object-oriented programming (OOP) organizes code using classes and objects. A class defines the structure and behavior of objects, while an object is an instance of a class.

### Inheritance

Inheritance allows one class to reuse the properties and methods of another class. It improves code reusability and helps developers organize large applications.

### Encapsulation

Encapsulation combines data and methods inside a class. It also helps control how the internal data of an object is accessed and modified.

# Artificial Intelligence

Artificial intelligence enables computers to perform tasks that typically require human intelligence. These tasks include learning, reasoning, understanding language, and solving problems.

## Machine Learning

Machine learning is a branch of artificial intelligence that enables systems to learn patterns from data. It is used in recommendation systems, fraud detection, and predictive analytics.

## Generative AI

Generative AI can create new content, including text, images, audio, and code. Large language models are an important part of generative AI and can power chatbots and virtual assistants.

# Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) combines document retrieval with language model generation. It retrieves relevant information from an external knowledge source before generating an answer.

## Text Splitting

Text splitting divides long documents into smaller chunks. These chunks can be converted into embeddings and stored in a vector database.

### Semantic Chunking

Semantic chunking uses embedding similarity to identify changes in meaning between text segments. It can help keep related information together and separate unrelated topics.

### Markdown Header Splitting

Markdown header splitting divides a Markdown document according to headings such as `#`, `##`, and `###`. It can also preserve heading information as metadata for each chunk.

# Flutter Development

Flutter is a framework for building cross-platform applications using the Dart programming language. It allows developers to create Android, iOS, web, and desktop applications.

## State Management with Riverpod

Riverpod helps manage application state and separate business logic from the user interface. It supports reactive state updates and dependency injection.

## API Integration with Dio

Dio is an HTTP client for Dart and Flutter. It supports GET, POST, PUT, PATCH, and DELETE requests, along with interceptors, timeouts, and error handling.'''
text = """
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def calculate_percentage(self):
        return sum(self.__marks) / len(self.__marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.__marks}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
        print(f"Grade: {self.calculate_grade()}")


class GraduateStudent(Student):
    def __init__(self, name, roll_no, marks, research_topic):
        super().__init__(name, roll_no, marks)
        self.research_topic = research_topic

    def display_details(self):
        super().display_details()
        print(f"Research Topic: {self.research_topic}")


def main():
    student1 = Student("Ali", 101, [85, 78, 92])
    student2 = GraduateStudent(
        "Sara", 202, [90, 88, 95], "Artificial Intelligence"
    )

    print("=== Regular Student ===")
    student1.display_details()

    print("\n=== Graduate Student ===")
    student2.display_details()


if __name__ == "__main__":
    main()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0,
    
)
splitter2 = RecursiveCharacterTextSplitter.from_language(
    language= Language.MARKDOWN,
    chunk_size = 150,
    chunk_overlap = 0,
    
)
chunks = splitter.split_text(text)
chunks2 = splitter2.split_text(text2)
print(chunks2)
print(len(chunks2))