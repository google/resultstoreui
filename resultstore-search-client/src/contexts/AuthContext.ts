import { createContext } from 'react';
export type TokenId = string;

export type AuthState = {
    tokenId: TokenId;
    setTokenId: (tokenId: TokenId) => void;
};

const defaultSetTokenId = (tokenId: TokenId) => {};

export const AuthContext = createContext<AuthState>({
    tokenId: '',
    setTokenId: defaultSetTokenId,
});
