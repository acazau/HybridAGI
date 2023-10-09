import os
from typing import List
from langchain.schema.embeddings import Embeddings
from langchain.schema.language_model import BaseLanguageModel

from .base import BaseProgramMemory

class ProgramMemory(BaseProgramMemory):
    """The Program Memory"""
    def __init__(
            self,
            index_name: str,
            redis_url: str,
            embedding: Embeddings,
            embedding_dim: int,
            llm: BaseLanguageModel,
            verbose: bool = True):
        """The program memory constructor"""
        super().__init__(
            index_name = index_name,
            redis_url = redis_url,
            embedding = embedding,
            embedding_dim = embedding_dim,
            llm = llm,
            verbose = verbose)

    def load_folders(
            self,
            folders: List[str]):
        """Method to load a library of programs, no check performed"""
        names = []
        programs = []
        for programs_folder in folders:
            for dirpath, dirnames, filenames in os.walk(programs_folder):
                for filename in filenames:
                    if filename.endswith(".cypher"):
                        program_name = filename.replace(".cypher", "")
                        try:
                            names.append(program_name)
                            source = os.path.join(dirpath, filename)
                            programs.append(open(source, "r").read())
                        except Exception:
                            pass
        self.add_programs(names = names, programs = programs)