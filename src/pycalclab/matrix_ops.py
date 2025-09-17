"""
Matrix operations for PyCalcLab

This module provides comprehensive matrix operations including
basic arithmetic, linear algebra operations, and matrix transformations.
"""

import math
from typing import List, Tuple, Union

Number = Union[int, float]
Matrix = List[List[Number]]
Vector = List[Number]


class MatrixCalculator:
    """Calculator for matrix and linear algebra operations."""
    
    @staticmethod
    def create_matrix(rows: int, cols: int, fill_value: Number = 0) -> Matrix:
        """Create a matrix with specified dimensions filled with a value."""
        return [[fill_value for _ in range(cols)] for _ in range(rows)]
    
    @staticmethod
    def identity_matrix(size: int) -> Matrix:
        """Create an identity matrix of given size."""
        matrix = MatrixCalculator.create_matrix(size, size, 0)
        for i in range(size):
            matrix[i][i] = 1
        return matrix
    
    @staticmethod
    def add_matrices(matrix1: Matrix, matrix2: Matrix) -> Matrix:
        """Add two matrices."""
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrices must have the same dimensions for addition")
        
        rows, cols = len(matrix1), len(matrix1[0])
        result = MatrixCalculator.create_matrix(rows, cols)
        
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        
        return result
    
    @staticmethod
    def subtract_matrices(matrix1: Matrix, matrix2: Matrix) -> Matrix:
        """Subtract matrix2 from matrix1."""
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrices must have the same dimensions for subtraction")
        
        rows, cols = len(matrix1), len(matrix1[0])
        result = MatrixCalculator.create_matrix(rows, cols)
        
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix1[i][j] - matrix2[i][j]
        
        return result
    
    @staticmethod
    def multiply_matrices(matrix1: Matrix, matrix2: Matrix) -> Matrix:
        """Multiply two matrices."""
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
        
        rows1, cols1 = len(matrix1), len(matrix1[0])
        rows2, cols2 = len(matrix2), len(matrix2[0])
        
        result = MatrixCalculator.create_matrix(rows1, cols2)
        
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        
        return result
    
    @staticmethod
    def scalar_multiply(matrix: Matrix, scalar: Number) -> Matrix:
        """Multiply a matrix by a scalar."""
        rows, cols = len(matrix), len(matrix[0])
        result = MatrixCalculator.create_matrix(rows, cols)
        
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix[i][j] * scalar
        
        return result
    
    @staticmethod
    def transpose(matrix: Matrix) -> Matrix:
        """Transpose a matrix."""
        rows, cols = len(matrix), len(matrix[0])
        result = MatrixCalculator.create_matrix(cols, rows)
        
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        
        return result
    
    @staticmethod
    def determinant_2x2(matrix: Matrix) -> Number:
        """Calculate determinant of a 2x2 matrix."""
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Matrix must be 2x2")
        
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    @staticmethod
    def determinant_3x3(matrix: Matrix) -> Number:
        """Calculate determinant of a 3x3 matrix."""
        if len(matrix) != 3 or len(matrix[0]) != 3:
            raise ValueError("Matrix must be 3x3")
        
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        
        return (a * (e * i - f * h) - 
                b * (d * i - f * g) + 
                c * (d * h - e * g))
    
    @staticmethod
    def dot_product(vector1: Vector, vector2: Vector) -> Number:
        """Calculate dot product of two vectors."""
        if len(vector1) != len(vector2):
            raise ValueError("Vectors must have the same length")
        
        return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
    
    @staticmethod
    def cross_product_3d(vector1: Vector, vector2: Vector) -> Vector:
        """Calculate cross product of two 3D vectors."""
        if len(vector1) != 3 or len(vector2) != 3:
            raise ValueError("Cross product requires 3D vectors")
        
        a1, a2, a3 = vector1
        b1, b2, b3 = vector2
        
        return [
            a2 * b3 - a3 * b2,
            a3 * b1 - a1 * b3,
            a1 * b2 - a2 * b1
        ]
    
    @staticmethod
    def vector_magnitude(vector: Vector) -> float:
        """Calculate magnitude (length) of a vector."""
        return math.sqrt(sum(x ** 2 for x in vector))
    
    @staticmethod
    def vector_normalize(vector: Vector) -> Vector:
        """Normalize a vector to unit length."""
        magnitude = MatrixCalculator.vector_magnitude(vector)
        if magnitude == 0:
            raise ValueError("Cannot normalize zero vector")
        
        return [x / magnitude for x in vector]
    
    @staticmethod
    def matrix_power(matrix: Matrix, n: int) -> Matrix:
        """Raise a square matrix to the power of n."""
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix must be square")
        
        if n == 0:
            return MatrixCalculator.identity_matrix(len(matrix))
        
        if n == 1:
            return [row[:] for row in matrix]  # Deep copy
        
        if n < 0:
            raise ValueError("Negative matrix powers not implemented")
        
        result = MatrixCalculator.identity_matrix(len(matrix))
        base = [row[:] for row in matrix]  # Deep copy
        
        while n > 0:
            if n % 2 == 1:
                result = MatrixCalculator.multiply_matrices(result, base)
            base = MatrixCalculator.multiply_matrices(base, base)
            n //= 2
        
        return result