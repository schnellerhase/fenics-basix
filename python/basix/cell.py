# Copyright (C) 2023-2024 Matthew Scroggs and Garth N. Wells
#
# This file is part of Basix (https://www.fenicsproject.org)
#
# SPDX-License-Identifier:    MIT
"""Functions to get cell geometry information and manipulate cell types."""

import numpy as np
import numpy.typing as npt

from basix._basixcpp import CellType
from basix._basixcpp import cell_facet_jacobians as _fj
from basix._basixcpp import cell_edge_jacobians as _ej
from basix._basixcpp import cell_facet_normals as _fn
from basix._basixcpp import cell_facet_orientations as _fo
from basix._basixcpp import cell_facet_outward_normals as _fon
from basix._basixcpp import cell_facet_reference_volumes as _frv
from basix._basixcpp import cell_volume as _v
from basix._basixcpp import geometry as _geometry
from basix._basixcpp import subentity_types as _sut
from basix._basixcpp import sub_entity_connectivity as _sec
from basix._basixcpp import sub_entity_type as _set
from basix._basixcpp import topology as _topology

__all__ = [
    "sub_entity_connectivity",
    "subentity_types",
    "volume",
    "edge_jacobians",
    "facet_jacobians",
    "facet_normals",
    "facet_orientations",
    "facet_outward_normals",
    "facet_reference_volumes",
]


def sub_entity_type(celltype: CellType, dim: int, index: int) -> CellType:
    """Cell type of a sub-entity.

    Args:
        celltype: cell type.
        dim: dimension of the sub-entity.
        index: index of the sub-entity

    Returns:
        The cell type of the sub-entity.
    """
    return _set(celltype, dim, index)


def sub_entity_connectivity(celltype: CellType) -> list[list[list[list[int]]]]:
    """Numbers of entities connected to each sub-entity of the cell.

    Args:
        celltype: cell type.

    Returns:
        Topology (vertex indices) for each dimension (0..tdim).
    """
    return _sec(celltype)


def volume(celltype: CellType) -> float:
    """Volume of a reference cell.

    Args:
        celltype: Cell type.

    Returns:
        Volume of the reference cell.
    """
    return _v(celltype)


def facet_jacobians(celltype: CellType) -> npt.NDArray:
    """Jacobians of the facets of a reference cell.

    Args:
        celltype: cell type.

    Returns:
        Jacobians of the facets.
    """
    return np.array(_fj(celltype))


def edge_jacobians(celltype: CellType) -> npt.NDArray:
    """Jacobians of the edges of a reference cell.

    Args:
        celltype: cell type.

    Returns:
        Jacobians of the edges.
    """
    return np.array(_ej(celltype))


def facet_normals(celltype: CellType) -> npt.NDArray:
    """Normals to the facets of a reference cell.

    These normals will be oriented using the low-to-high ordering of the
    facet.

    Args:
        celltype: Cell type.

    Returns:
        Normals to the facets.
    """
    return np.array(_fn(celltype))


def facet_orientations(celltype: CellType) -> list[int]:
    """Orientations of the facets of a reference cell.

    This returns a list of bools that are ``True`` if the facet normal
    points outwards and ``False`` otherwise.

    Args:
        celltype: Cell type.

    Returns:
        Facet orientations.
    """
    return _fo(celltype)


def facet_outward_normals(celltype: CellType) -> npt.NDArray:
    """Normals to the facets of a reference cell.

    These normals will be oriented to be pointing outwards.

    Args:
        celltype: Cell type.

    Returns:
        Normals to the facets.
    """
    return np.array(_fon(celltype))


def facet_reference_volumes(celltype: CellType) -> npt.NDArray:
    """Reference volumes of the facets of a reference cell.

    Args:
        celltype: Cell type.

    Returns:
        Reference volumes.
    """
    return np.array(_frv(celltype))


def geometry(celltype: CellType) -> npt.NDArray:
    """Cell geometry.

    Args:
        celltype: Cell type.

    Returns:
        Vertices of the cell.
    """
    return np.array(_geometry(celltype))


def topology(celltype: CellType) -> list[list[list[int]]]:
    """Cell topology.

    Args:
        celltype: Cell type.

    Returns:
        Vertex indices for each sub-entity of the cell.
    """
    return _topology(celltype)


def subentity_types(celltype: CellType) -> list[list[CellType]]:
    """Get the types of the subentities of a reference cell.

    Args:
        celltype: Cell type.

    Returns:
        Cell types for each sub-entity of the cell. Indices are (tdim, entity).
    """
    return _sut(celltype)
