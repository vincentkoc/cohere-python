import sseclient
import json
from concurrent.futures import Future
from typing import Any, Dict, Iterator, List, NamedTuple, Optional, Union

from cohere.response import AsyncAttribute, CohereObject

TokenLikelihood = NamedTuple("TokenLikelihood", [("token", str), ("likelihood", float)])


class Generation(CohereObject, str):

    def __new__(cls, text: str, *_, **__):
        return str.__new__(cls, text)

    def __init__(self, text: str, likelihood: float, token_likelihoods: List[TokenLikelihood]) -> None:
        self.text = text
        self.likelihood = likelihood
        self.token_likelihoods = token_likelihoods

    def __str__(self) -> str:
        return str(self.text)

    def __len__(self) -> int:
        return len(self.text)

    def __getitem__(self, index) -> str:
        return self.text[index]


class Generations(CohereObject):

    def __init__(self,
                 return_likelihoods: str,
                 response: Optional[Dict[str, Any]] = None,
                 *,
                 _future: Optional[Future] = None) -> None:
        self.generations: Union[AsyncAttribute, List[Generation]] = None
        self.return_likelihoods = return_likelihoods
        if _future is not None:
            self._init_from_future(_future)
        else:
            assert response is not None
            self.generations = self._generations(response)

    def _init_from_future(self, future: Future):
        self.generations = AsyncAttribute(future, self._generations)

    def _generations(self, response: Dict[str, Any]) -> List[Generation]:
        generations: List[Generation] = []
        for gen in response['generations']:
            likelihood = None
            token_likelihoods = None
            if self.return_likelihoods in ['GENERATION', 'ALL']:
                likelihood = gen['likelihood']
            if 'token_likelihoods' in gen.keys():
                token_likelihoods = []
                for likelihoods in gen['token_likelihoods']:
                    token_likelihood = likelihoods['likelihood'] if 'likelihood' in likelihoods.keys() else None
                    token_likelihoods.append(TokenLikelihood(likelihoods['token'], token_likelihood))
            generations.append(Generation(gen['text'], likelihood, token_likelihoods))

        return generations

    def __str__(self) -> str:
        return str(self.generations)

    def __iter__(self) -> Iterator:
        return iter(self.generations)

    def __getitem__(self, index) -> Generation:
        return self.generations[index]


class GenerationStream(CohereObject):

    def __init__(self,
                 return_likelihoods: str,
                 response: Optional[Dict[str, Any]] = None,
                 *,
                 _future: Optional[Future] = None) -> None:
        self.curr_generation = None
        self.return_likelihoods = return_likelihoods
        self.client = None
        if _future is not None:
            self.client = sseclient.SSEClient(_future.result())
        else:
            assert response is not None
            self.client = sseclient.SSEClient(response)

    def stream(self):
        for event in self.client.events():
            gen = json.loads(event.data)
            likelihood = None
            if self.return_likelihoods in ['GENERATION', 'ALL'] and 'likelihood' in gen.keys():
                likelihood = gen['likelihood']
            self.curr_generation = Generation(gen["text"], likelihood, None)
            yield self.curr_generation

    def response(self):
        return self.curr_generation
